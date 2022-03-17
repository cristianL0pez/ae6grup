from models.methods_list import Methods_list
from models.customer import Customer

class Customer_register(Methods_list):
    def __init__(self):
        super().__init__()

    def create(self, rut, name, last, email, balance):
        costumer = Customer(rut, name, last, email, balance)

    def buy(self, price, id_):
        customer = super().search_for(id_)
        if (customer['_Customer__balance']) >= price:
            customer['_Customer__balance'] -= price
            return customer['_Customer__balance']
        else:
            return 'El cliente no tiene el saldo suficiente'