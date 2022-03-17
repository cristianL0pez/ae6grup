class Seller:
    def __init__(self, id_seller,rut, name, last, section):
        self.id_seller = id_seller
        self.rut = rut
        self.name = name
        self.last = last
        self.section = section
        self.__profit = 0.05

    def get(self):
        return self.__dict__

    def get_comission(self):
        return self.__profit
    
    def sell(self):
        pass