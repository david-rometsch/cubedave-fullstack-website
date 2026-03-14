import json
import os
from contextlib import contextmanager

import uvicorn

# fastapi imports
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  # included in fastapi.

# sqlalchemy imports
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

if os.path.exists("database.db"):
    os.remove("database.db")  # avoid confilcts with pre-existing table
    print("removed db...")
    # exit()
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


def get_db():  # without contextmanager for post/Depends()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    size = Column(String(100))
    brand = Column(String(100), nullable=False)
    info = Column(String, nullable=True)
    category = Column(String(100), nullable=False)
    description = Column(String(100), nullable=True)
    image = Column(Text, nullable=True)

    @classmethod
    def read_all(cls, session) -> list[type]:
        """Return list of all instances or []"""
        return session.query(cls).all()


# pydantic-interface
class ProductCreateSchema(BaseModel):
    name: str
    size: str
    brand: str
    info: str | None = None
    category: str
    description: str
    image: str | None = None


class ProductSchema(ProductCreateSchema):
    id: int

    class Config:
        from_attributes = True  # only allows SQLAlchemy-Objekte


# create tables
Base.metadata.create_all(engine)

if True:  # seed demodata - set false later

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
        products = Product.read_all(session)
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
        products = Product.read_all(session)
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
