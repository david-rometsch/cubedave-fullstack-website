import json
import os
from contextlib import contextmanager


# fastapi imports
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from models import Base, Order, OrderRequest, OrderSchema, Product, ProductCreateSchema, ProductOrder, ProductSchema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://cubedave.ch"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# create engine
engine = create_engine("sqlite:///database.db")
print("created db...")


# create Session-object
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# yield session using context manager
@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


# without contextmanager for e.g. post/Depends()
def get_db():  
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create tables
Base.metadata.create_all(engine)


# seed  if db is empty
with get_session() as session:
    if session.query(Product).count() == 0 :  
        def load_json_product():
            with open("./static/product.json", "r", encoding="utf-8") as f:
                dict_of_product = json.load(f)
            # print("dict of product : ", dict_of_product)
            return dict_of_product

        # seed product
        seed_product = load_json_product()
        with get_session() as session:
            if session.query(Product).count() == 0:  # only if no products available.
                for s_product in seed_product["product"]:
                    product = Product(**s_product)
                    session.add(product)
                    print("added", product)


# ==== API ====
@app.get("/api/all_product", response_model=list[ProductSchema])
async def load_product():
    with get_session() as session:
        products = session.query(Product).all()
        return [ProductSchema.model_validate(p) for p in products]


# add product to db (also for update)
@app.post("/api/add_product")
def add_product(
    product: ProductCreateSchema,
    db: Session = Depends(get_db),
):
    db_product = Product(**product.model_dump())  # model_dup from pydantic
    db.add(db_product)
    db.commit()
    db.refresh(db_product)  # check if db entry succeeded
    return db_product  # 200 if product added


# save current db state to product.json (overwrites seed data)
@app.post("/api/save_data")
def save_data():
    with get_session() as session:
        products = session.query(Product).all()
        data = []
        for p in products:
            d = ProductSchema.model_validate(p).model_dump(exclude={'id'})
            # move image to end
            image = d.pop('image', None)
            d['image'] = image
            data.append(d)
    with open("./static/product.json", "w", encoding="utf-8") as f:
        json.dump({"product": data}, f, ensure_ascii=False, indent=2)
    return {"status": "saved"}


# delete product by id
@app.delete("/api/delete_product/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.get(Product, product_id)
    db.delete(db_product)
    db.commit()
    return {"status": "deleted"}


# create order from cart
@app.post("/api/order")
def create_order(order_req: OrderRequest, db: Session = Depends(get_db)):
    order = Order(customer_name=order_req.customer_name)
    db.add(order)
    db.flush()  # get order.id before commit
    for item in order_req.items:
        po = ProductOrder(order_id=order.id, product_id=item["product_id"], quantity=item["quantity"])
        db.add(po)
    db.commit()
    db.refresh(order)
    return {"status": "ordered", "order_id": order.id}


# get all orders with total
@app.get("/api/orders")
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    result = []
    for o in orders:
        total = sum(
            (po.product.price or 0) * po.quantity for po in o.product_associations
        )
        result.append({"id": o.id, "customer_name": o.customer_name, "total": round(total, 2)})
    return result


# get single order detail
@app.get("/api/order/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    o = db.get(Order, order_id)
    items = [
        {
            "product_name": po.product.name,
            "price": po.product.price,
            "quantity": po.quantity,
            "subtotal": round((po.product.price or 0) * po.quantity, 2),
        }
        for po in o.product_associations
    ]
    total = round(sum(i["subtotal"] for i in items), 2)
    return {"id": o.id, "customer_name": o.customer_name, "total": total, "items": items}


# put to update product (one or multiple fields at once)
@app.put("/api/update_product/{product_id}")
def update_product(
    product_id: int, product: ProductSchema, db: Session = Depends(get_db)
):
    db_product = db.get(Product, product_id)
    for key, value in product.model_dump(exclude={'id'}).items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product
