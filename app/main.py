"""
main.py — FastAPI application entry point.
Handles database setup, seeding, and all REST API endpoints.
"""

import json
from contextlib import contextmanager

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from models import Base, Order, OrderRequest, Product, ProductCreateSchema, ProductOrder, ProductSchema, Visit

app = FastAPI()

# Allow requests from the local dev server and the production domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://cubedave.ch"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLite database engine
engine = create_engine("sqlite:///database.db")

# Session factory — autocommit disabled so commits are explicit
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_session():
    """Context manager for database sessions used in startup/seeding code."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


def get_db():
    """Dependency-injected session for FastAPI route handlers."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create all tables defined in models if they don't exist yet
Base.metadata.create_all(engine)

# Seed the database with products from product.json if the table is empty
with get_session() as session:
    if session.query(Product).count() == 0:
        with open("./static/product.json", "r", encoding="utf-8") as f:
            seed_data = json.load(f)
        with get_session() as session:
            for item in seed_data["product"]:
                session.add(Product(**item))


# ==== API endpoints ====

@app.get("/api/all_product", response_model=list[ProductSchema])
async def load_product():
    """Return all products."""
    with get_session() as session:
        products = session.query(Product).all()
        return [ProductSchema.model_validate(p) for p in products]


@app.post("/api/add_product")
def add_product(product: ProductCreateSchema, db: Session = Depends(get_db)):
    """Add a new product to the database."""
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.post("/api/save_data")
def save_data():
    """Persist the current database state back to product.json."""
    with get_session() as session:
        products = session.query(Product).all()
        data = []
        for p in products:
            d = ProductSchema.model_validate(p).model_dump(exclude={'id'})
            image = d.pop('image', None)
            d['image'] = image  # move image field to end
            data.append(d)
    with open("./static/product.json", "w", encoding="utf-8") as f:
        json.dump({"product": data}, f, ensure_ascii=False, indent=2)
    return {"status": "saved"}


@app.delete("/api/delete_product/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Delete a product by its ID."""
    db_product = db.get(Product, product_id)
    db.delete(db_product)
    db.commit()
    return {"status": "deleted"}


@app.post("/api/order")
def create_order(order_req: OrderRequest, db: Session = Depends(get_db)):
    """Create a new order with all its line items from the cart."""
    order = Order(customer_name=order_req.customer_name)
    db.add(order)
    db.flush()  # flush to get order.id before inserting line items
    for item in order_req.items:
        po = ProductOrder(order_id=order.id, product_id=item["product_id"], quantity=item["quantity"])
        db.add(po)
    db.commit()
    db.refresh(order)
    return {"status": "ordered", "order_id": order.id}


@app.get("/api/orders")
def get_orders(db: Session = Depends(get_db)):
    """Return all orders with their computed total price."""
    orders = db.query(Order).all()
    result = []
    for o in orders:
        total = sum((po.product.price or 0) * po.quantity for po in o.product_associations)
        result.append({"id": o.id, "customer_name": o.customer_name, "total": round(total, 2)})
    return result


@app.get("/api/order/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    """Return a single order with its line items and total."""
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


@app.post("/api/visit")
def record_visit(db: Session = Depends(get_db)):
    """Record a shop visit."""
    db.add(Visit())
    db.commit()
    return {"status": "recorded"}


@app.get("/api/visits")
def get_visits(db: Session = Depends(get_db)):
    """Return total number of shop visits."""
    return {"count": db.query(Visit).count()}


@app.post("/api/restore_data")
def restore_data():
    """Delete all products and reload from the original seed file (product_default.json)."""
    with get_session() as session:
        session.query(Product).delete()
        with open("./static/product_default.json", "r", encoding="utf-8") as f:
            seed_data = json.load(f)
        for item in seed_data["product"]:
            session.add(Product(**item))
    return {"status": "restored"}


@app.put("/api/update_product/{product_id}")
def update_product(product_id: int, product: ProductSchema, db: Session = Depends(get_db)):
    """Update one or more fields of an existing product."""
    db_product = db.get(Product, product_id)
    for key, value in product.model_dump(exclude={'id'}).items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product
