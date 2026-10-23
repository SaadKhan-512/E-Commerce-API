from sqlalchemy import Column, String, Integer, ForeignKey
from database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String, nullable=False)

class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, unique=True)
    
    price = Column(Integer, nullable=False)
    stock_quantity = Column(Integer, nullable=False)

class Carts(Base):
    __tablename__ =  "carts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

class Cart_Items(Base):
    __tablename__ = 'cart_items'

    cart_item_id = Column(Integer, nullable=False, primary_key=True)
    quantity = Column(Integer, nullable=False)
    