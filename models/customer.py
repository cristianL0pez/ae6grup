# from datetime import datetime
# datetime.today().strftime('%d-%m-%Y')
class Customer:
    def __init__(self, id_customer, rut, name, surname, email, join_date, balance):
        self.id_customer = id_customer
        self.rut = rut
        self.name = name
        self.surname = surname
        self.email = email
        self.join_date = join_date
        self.__balance = balance
        self.cart = []

    def get(self):
        return self.__dict__
    
    def getbalance(self):
        return self.__balance
    
    def setbalance(self, balance):
        self.__balance -= balance