from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


# ==== product model ====
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
    image = Column(Text, nullable=True)

    order_associations = relationship("ProductOrder", back_populates="product")


# pydantic schemes
class ProductCreateSchema(BaseModel):
    name: str
    size: str
    brand: str
    info: str | None = None
    category: str
    price: float | None = None
    description: str
    image: str | None = None


# extension for basic scheme including id (used in update)
class ProductSchema(ProductCreateSchema):
    id: int
    # model_config makes sqlalchemy models readable for pydantic
    model_config = ConfigDict(from_attributes=True)


# ==== Order model ====
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    customer_name = Column(String(100), nullable=False)

    product_associations = relationship("ProductOrder", back_populates="order")


# ==== ProductOrder association object including quantity field ====
class ProductOrder(Base):
    __tablename__ = "product_orders"

    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), primary_key=True)
    quantity = Column(Integer, default=1)

    product = relationship("Product", back_populates="order_associations")
    order = relationship("Order", back_populates="product_associations")


# pydantic
class ProductOrderSchema(BaseModel):
    quantity: int
    product: ProductSchema

    model_config = ConfigDict(from_attributes=True)


# order pydantic scheme
class OrderSchema(BaseModel):
    id: int
    customer_name: str
    product_associations: list[ProductOrderSchema]

    model_config = ConfigDict(from_attributes=True)


class OrderRequest(BaseModel):
    customer_name: str
    items: list[dict]  # [{product_id, quantity}]
