from models.methods_list import Methods_list
from models.product import Product

class Warehouse(Methods_list):
    def __init__(self):
        super().__init__()

    def create(self, SKU, name, category, stock, price, tax, made_in, *supplier):
        product = Product(SKU, name, category, stock, price, tax, made_in, *supplier)
        super().add(product)
    
    def stock_update(self, sku, qty):
        product = super().search_for(sku)
        if product['stock'] >= qty:
            product['stock'] -= qty
            return product
        else:
            return 'No tenemos esa cantidad del producto'