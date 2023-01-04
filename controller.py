from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
import re

from models import Customer, Order, Product, Base


db_path = 'sqlite:///store.db'
engine = create_engine(db_path, echo=False)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()



class Authentication():
    @classmethod
    def email_is_valid(self, email):
        email_regex = r'[\w\d.]+@[\w\d.]+'
        if re.fullmatch(email_regex, email):
            return True
        else:
            return False
    
    @classmethod
    def password_is_valid(self, password):
        password_regex = r'([\W]*[\w]+[\d]+[!]*)'
        if len(password) > 8 and re.fullmatch(password_regex, password):
            return True
        else:
            return False
    

    @classmethod
    def phonenumber_is_valid(self, phone_number):
        phone_regex = r'([\d]+)'
        if re.fullmatch(phone_regex, phone_number):
            return True
        else:
            return False

    
    @classmethod
    def full_name_is_valid(self, full_name):
        full_name_regex = r'[\w]+[\s]+[\w]+'
        if re.fullmatch(full_name_regex, full_name):
            return True
        else:
            return False


    @classmethod
    def encrypt_password(self, password):
        pass


    @classmethod
    def create_user(self, email, full_name, phone_number, password):
        pass


    @classmethod
    def authenticate_user(self, email, password):
        pass


    @classmethod
    def delete_user(self, id):
        pass


    @classmethod
    def update_user_details(self, id, values):
        pass


    @classmethod
    def get_user(self, id):
        pass
    

 





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