import datetime
import uuid
from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.bar_code = str(uuid.uuid4())

    @abstractmethod
    def get_total_value(self):
        pass


class FoodProduct(Product):
    def __init__(self, name, price, quantity, description, expiration_date):
        super().__init__(name, price, quantity, description)

        if isinstance(expiration_date, str):
            self.expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
        elif isinstance(expiration_date, datetime.datetime):
            self.expiration_date = expiration_date.date()
        else:
            self.expiration_date = expiration_date

    def get_total_value(self):
        return self.price * self.quantity

    def is_expired(self):
        return datetime.date.today() > self.expiration_date


class ElectronicProduct(Product):
    def __init__(self, name, price, quantity, description, warranty_date):
        super().__init__(name, price, quantity, description)

        if isinstance(warranty_date, str):
            self.warranty_date = datetime.datetime.strptime(warranty_date, "%Y-%m-%d").date()
        elif isinstance(warranty_date, datetime.datetime):
            self.warranty_date = warranty_date.date()
        else:
            self.warranty_date = warranty_date

    def get_total_value(self):
        return self.price * self.quantity

    def is_under_warranty(self):
        return datetime.date.today() <= self.warranty_date


class ClothingProduct(Product):
    def __init__(self, name, price, quantity, description, color, size, material):
        super().__init__(name, price, quantity, description)
        self.color = color
        self.size = size
        self.material = material

    def get_total_value(self):
        return self.price * self.quantity
