class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Warehouse:
    def __init__(self):
        self.products = []

    def add(self, prod):
        self.products.append(prod)

    def total_value(self):
        return sum([x.price for x in self.products])

    def product_count(self):
        return len(self.products)
