class Supplier:
    def __init__(self, id_supplier, rut, business_name, name, legal_personality = True, country = 'Chile'):
        self.id_supplier = id_supplier
        self.rut = rut
        self.business_name = business_name
        self.name = name
        self.legal_personality = legal_personality
        self.country = country

    def get(self):
        return self.__dict__  