class Product:
    def __init__(self, name, price, quantity, description, unique_code):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.unique_code = unique_code

    def __str__(self):
        return f"Product(Name={self.name} , Price={self.price}, Quantity={self.quantity})"


if __name__ == '__main__':
    p = Product("S25+", 1500, 3, "Latest smartphone from Samsung", 564556491)
    print(p)
