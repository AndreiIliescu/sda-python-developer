import datetime
import json
from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price, quantity, description, bar_code):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.bar_code = bar_code

    @abstractmethod
    def get_total_value(self):
        pass


class FoodProduct(Product):
    def __init__(self, name, price, quantity, description, bar_code, expiration_date):
        super().__init__(name, price, quantity, description, bar_code)

        if isinstance(expiration_date, str):
            self.expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
        elif isinstance(expiration_date, datetime.datetime):
            self.expiration_date = expiration_date.date()
        elif isinstance(expiration_date, datetime.date):
            self.expiration_date = expiration_date
        else:
            raise ValueError("Invalid expiration date format. Must be a string, datetime, or date format.")

    def get_total_value(self):
        return self.price * self.quantity

    def is_expired(self):
        return self.expiration_date < datetime.date.today()


class ElectronicProduct(Product):
    def __init__(self, name, price, quantity, description, bar_code, warranty_date):
        super().__init__(name, price, quantity, description, bar_code)

        if isinstance(warranty_date, str):
            self.warranty_date = datetime.datetime.strptime(warranty_date, "%Y-%m-%d").date()
        elif isinstance(warranty_date, datetime.datetime):
            self.warranty_date = warranty_date.date()
        elif isinstance(warranty_date, datetime.date):
            self.warranty_date = warranty_date
        else:
            raise ValueError("Invalid warranty date format. Must be a string, datetime, or date format.")

    def get_total_value(self):
        return self.price * self.quantity

    def is_under_warranty(self):
        return self.warranty_date >= datetime.date.today()


class ClothingProduct(Product):
    def __init__(self, name, price, quantity, description, bar_code):
        super().__init__(name, price, quantity, description, bar_code)

    def get_total_value(self):
        return self.price * self.quantity


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        for i in self.products:
            if i.bar_code == product.bar_code:
                print(f"The product already exists.")
                return
        self.products.append(product)

    def print_products(self):
        if not self.products:
            print("No products in the warehouse.")
            return

        header = (f"{'Name':20} {'Price':10} {'Quantity':10} {'Description':30} {'Bar Code':12} {'Type':15} "
                  f"{'Extra Info':20}")
        print(header)
        print("-" * len(header))

        for p in self.products:
            prod_type = type(p).__name__
            extra_info = ""
            if hasattr(p, "expiration_date"):
                extra_info = f"Expires on: {p.expiration_date}"
            elif hasattr(p, "warranty_date"):
                extra_info = f"In warranty until: {p.warranty_date}"

            print(f"{p.name:20} {p.price:<10.2f} {p.quantity:<10} {p.description:30} {p.bar_code:<12} {prod_type:15} "
                  f"{extra_info:20}")

    def save_products(self, filename):
        data = []
        for p in self.products:
            prod_dict = {
                "type": type(p).__name__,
                "name": p.name,
                "price": p.price,
                "quantity": p.quantity,
                "description": p.description,
                "bar_code": p.bar_code
            }
            if hasattr(p, "expiration_date"):
                prod_dict["expiration_date"] = p.expiration_date.isoformat()
            if hasattr(p, "warranty_date"):
                prod_dict["warranty_date"] = p.warranty_date.isoformat()

            data.append(prod_dict)

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Products saved to {filename}")


    def load_products(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            self.products = []

            for item in data:
                prod_type = item["type"]
                if prod_type == "FoodProduct":
                    product = FoodProduct(
                        item["name"],
                        item["price"],
                        item["quantity"],
                        item["description"],
                        item["bar_code"],
                        item["expiration_date"]
                    )
                elif prod_type == "ElectronicProduct":
                    product = ElectronicProduct(
                        item["name"],
                        item["price"],
                        item["quantity"],
                        item["description"],
                        item["bar_code"],
                        item["warranty_date"]
                    )
                elif prod_type == "ClothingProduct":
                    product = ClothingProduct(
                        item["name"],
                        item["price"],
                        item["quantity"],
                        item["description"],
                        item["bar_code"]
                    )
                else:
                    print(f"Unknown product type: {prod_type}, skipping.")
                    continue

                self.products.append(product)

            print(f"Products loaded from {filename}")

        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON file.")

    def remove_product(self, bar_code):
        initial_count = len(self.products)
        self.products = [p for p in self.products if p.bar_code != bar_code]
        removed_count = initial_count - len(self.products)

        if removed_count > 0:
            print(f"Removed {removed_count} product(s) with bar code {bar_code}.")
        else:
            print(f"No product found with bar code {bar_code}.")


warehouse = Warehouse("Warehouse")

product1 = FoodProduct("Apple", 10.19, 50, "Red bio apple", 1427685,
                       "2025-08-17")
print(product1.get_total_value())
print(product1.is_expired())

print()

product2 = ElectronicProduct("Samsung Galaxy A55 5G", 789.99, 10,
                             "Smartphone Samsung", 7569128, datetime.date(2027, 6, 14))
print(product2.get_total_value())
print(product2.is_under_warranty())

print()

product3 = ClothingProduct("T-shirt", 79.99, 100, "Light Blue cotton T-shirt",
                           5671362)
print(product3.get_total_value())

print()

warehouse.add_product(product1)
warehouse.add_product(product2)
warehouse.add_product(product3)

warehouse.print_products()

print()

warehouse.save_products("products.json")

print()

warehouse.remove_product(7569128)

print()

warehouse2 = Warehouse("Backup Warehouse")
warehouse2.load_products("products.json")
