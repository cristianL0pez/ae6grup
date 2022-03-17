from datetime import datetime
from helpers import uuid_generator

class Customer:
    def __init__(self, rut, name, last, email, balance):
        self.id_customer = uuid_generator.create(8) 
        self.rut = rut
        self.name = name
        self.last = last
        self.email = email
        self.join_date = datetime.today().strftime('%d-%m-%Y')
        self.__balance = balance
        self.cart = []

    def get(self):
        return self.__dict__
    
    def getbalance(self):
        return self.__balance
    
    def setbalance(self, balance):
        self.__balance -= balance