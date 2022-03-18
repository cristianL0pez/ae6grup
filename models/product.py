from models.supplier import Supplier

class Product():
    def __init__(self, SKU, name, category, stock, price, tax, made_in, *supplier):
        self.SKU = SKU
        self.name = name
        self.category = category
        self.stock = stock
        self.price = price
        self.tax = tax
        self.made_in = made_in
        self.supplier = Supplier(supplier)

    def get(self):
        return {
            'SKU': self.SKU,
            'name': self.name,
            'category': self.category,
            'stock': self.stock,
            'price': self.price,
            'tax': self.tax,
            'made_in': self.made_in,
            'supplier': self.get_supplier(),
        }

    def get_supplier(self):
        return self.proveedor.get()

    def get_impuesto(self):
        return self.__impuesto