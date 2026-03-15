"""
models.py — SQLAlchemy ORM models and Pydantic validation schemas.
"""

from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


# ==== ORM models ====

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    size = Column(String(100))
    brand = Column(String(100), nullable=False)
    info = Column(String, nullable=True)
    category = Column(String(100), nullable=False)
    price = Column(Float, nullable=True)
    description = Column(String(100), nullable=True)
    image = Column(Text, nullable=True)  # stored as base64 data URL

    order_associations = relationship("ProductOrder", back_populates="product")


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    customer_name = Column(String(100), nullable=False)

    product_associations = relationship("ProductOrder", back_populates="order")


class ProductOrder(Base):
    """Association table between Order and Product, carrying the ordered quantity."""
    __tablename__ = "product_orders"

    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), primary_key=True)
    quantity = Column(Integer, default=1)

    product = relationship("Product", back_populates="order_associations")
    order = relationship("Order", back_populates="product_associations")


# ==== Pydantic schemas ====

class ProductCreateSchema(BaseModel):
    """Validates incoming product data for creation (no id required)."""
    name: str
    size: str
    brand: str
    info: str | None = None
    category: str
    price: float | None = None
    description: str
    image: str | None = None


class ProductSchema(ProductCreateSchema):
    """Extends ProductCreateSchema with id — used for responses and updates."""
    id: int
    model_config = ConfigDict(from_attributes=True)


class ProductOrderSchema(BaseModel):
    quantity: int
    product: ProductSchema

    model_config = ConfigDict(from_attributes=True)


class OrderSchema(BaseModel):
    id: int
    customer_name: str
    product_associations: list[ProductOrderSchema]

    model_config = ConfigDict(from_attributes=True)


class OrderRequest(BaseModel):
    """Validates the order payload sent from the cart."""
    customer_name: str
    items: list[dict]  # list of {product_id, quantity}
