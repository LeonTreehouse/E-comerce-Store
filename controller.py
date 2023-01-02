from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker

from models import Customer, Order, Product, Base


db_path = 'sqlite:///store.db'
engine = create_engine(db_path, echo=False)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# Class Authentication
# Email, Password, Phone Number, Full name is valid
# encrypt password
# getting/delete/create/update User

# Class Order
# get/remove/create Order
# Refund? 


#Class Products
#get products
#Update quantity of the products
#check stock if there is enough for the customer to order
#if 0 say out of stock
#Delete products