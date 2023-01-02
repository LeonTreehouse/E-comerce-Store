from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ ='customers'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    full_name = Column(String)
    phone_number = Column(Integer)
    password = Column(String)
    purchases = relationship("order", back_populates="customer",
                            cascade="all, delete, delete-orphan")


    def __repr__(self):
        return f'<User fullname={self.full_name}>'



class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    product_quantity = Column(Integer)
    customer = relationship("Customer", back_populates="order")
    products = relationship("Product", back_populates="Order", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f'Order Number: {self.id}\nProduct: {self.products}\nQuantity: {self.product_quantity}'


class Product(Base):
    __tablename__ = 'products'
    
    item_name = Column(String)
    order_id = Column(Integer, ForeignKey('orders.id'))
    quantity = Column(Integer)
    order = relationship("Order", back_populates="product",
                        cascade="all, delete, delete-orphan")

    
    def __repr__(self):
        return f'<Product name={self.item_name}>'
    
