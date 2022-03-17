from helpers import uuid_generator
class Supplier:
    def __init__(self, rut, business_name, name, legal_personality = True, country = 'Chile'):
        self.id_supplier = uuid_generator.create(8)
        self.rut = rut
        self.business_name = business_name
        self.name = name
        self.legal_personality = legal_personality
        self.country = country

    def get(self):
        return self.__dict__  