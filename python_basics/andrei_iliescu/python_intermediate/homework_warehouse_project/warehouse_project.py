# import datetime
# import json
# from abc import ABC, abstractmethod
#
#
# class Product(ABC):
#     def __init__(self, name, price, quantity, description, bar_code):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.description = description
#         self.bar_code = bar_code
#
#     @abstractmethod
#     def get_total_value(self):
#         pass
#
#
# class FoodProduct(Product):
#     def __init__(self, name, price, quantity, description, bar_code, expiration_date):
#         super().__init__(name, price, quantity, description, bar_code)
#
#         if isinstance(expiration_date, str):
#             self.expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
#         elif isinstance(expiration_date, datetime.datetime):
#             self.expiration_date = expiration_date.date()
#         elif isinstance(expiration_date, datetime.date):
#             self.expiration_date = expiration_date
#         else:
#             raise ValueError("Invalid expiration date format. Must be a string, datetime, or date format.")
#
#     def get_total_value(self):
#         return self.price * self.quantity
#
#     def is_expired(self):
#         return self.expiration_date < datetime.date.today()
#
#
# class ElectronicProduct(Product):
#     def __init__(self, name, price, quantity, description, bar_code, warranty_date):
#         super().__init__(name, price, quantity, description, bar_code)
#
#         if isinstance(warranty_date, str):
#             self.warranty_date = datetime.datetime.strptime(warranty_date, "%Y-%m-%d").date()
#         elif isinstance(warranty_date, datetime.datetime):
#             self.warranty_date = warranty_date.date()
#         elif isinstance(warranty_date, datetime.date):
#             self.warranty_date = warranty_date
#         else:
#             raise ValueError("Invalid warranty date format. Must be a string, datetime, or date format.")
#
#     def get_total_value(self):
#         return self.price * self.quantity
#
#     def is_under_warranty(self):
#         return self.warranty_date >= datetime.date.today()
#
#
# class ClothingProduct(Product):
#     def __init__(self, name, price, quantity, description, bar_code):
#         super().__init__(name, price, quantity, description, bar_code)
#
#     def get_total_value(self):
#         return self.price * self.quantity
#
#
# class Warehouse:
#     def __init__(self, name):
#         self.name = name
#         self.products = []
#
#     def add_product(self, product):
#         for i in self.products:
#             if i.bar_code == product.bar_code:
#                 print(f"The product already exists.")
#                 return
#         self.products.append(product)
#
#     def print_products(self):
#         if not self.products:
#             print("No products in the warehouse.")
#             return
#
#         header = (f"{'Name':20} {'Price':10} {'Quantity':10} {'Description':30} {'Bar Code':12} {'Type':15} "
#                   f"{'Extra Info':20}")
#         print(header)
#         print("-" * len(header))
#
#         for p in self.products:
#             prod_type = type(p).__name__
#             extra_info = ""
#             if hasattr(p, "expiration_date"):
#                 extra_info = f"Expires on: {p.expiration_date}"
#             elif hasattr(p, "warranty_date"):
#                 extra_info = f"In warranty until: {p.warranty_date}"
#
#             print(f"{p.name:20} {p.price:<10.2f} {p.quantity:<10} {p.description:30} {p.bar_code:<12} {prod_type:15} "
#                   f"{extra_info:20}")
#
#     def save_products(self, filename):
#         data = []
#         for p in self.products:
#             prod_dict = {
#                 "type": type(p).__name__,
#                 "name": p.name,
#                 "price": p.price,
#                 "quantity": p.quantity,
#                 "description": p.description,
#                 "bar_code": p.bar_code
#             }
#             if hasattr(p, "expiration_date"):
#                 prod_dict["expiration_date"] = p.expiration_date.isoformat()
#             if hasattr(p, "warranty_date"):
#                 prod_dict["warranty_date"] = p.warranty_date.isoformat()
#
#             data.append(prod_dict)
#
#         with open(filename, "w") as f:
#             json.dump(data, f, indent=4)
#         print(f"Products saved to {filename}")
#
#     def remove_product(self, bar_code):
#         initial_count = len(self.products)
#         self.products = [product for product in self.products if product.bar_code != bar_code]
#         remove_cont = initial_count - len(self.products)
#
#         if remove_cont > 0:
#             print(f"Removed {remove_cont} product with bar code {bar_code}")
#         else:
#             print(f"No product found with bar code {bar_code}")
#
#     def load_products(self):
#         pass
#
#
# warehouse = Warehouse("Warehouse")
#
# food_product1 = FoodProduct("Apple", 10.19, 50, "Red bio apple", 1427685,
#                        "2025-08-17")
# print(food_product1.get_total_value())
# print(food_product1.is_expired())
# food_product2 = FoodProduct("Banana", 8.99, 12, "Chiquita - Fresh Banana",
#                             5674168, "2025-08-15")
#
# print()
#
# electronic_product1 = ElectronicProduct("Samsung Galaxy A55 5G", 1799.99, 10,
#                              "Smartphone Samsung", 7569128, datetime.date(2027, 6, 14))
# print(electronic_product1.get_total_value())
# print(electronic_product1.is_under_warranty())
# electronic_product2 = ElectronicProduct("Macbook Air 13", 5099.90, 5,
#                                         "Laptop APPLE MacBook Air 13", 8723149,
#                                         "2027-09-30")
#
#
# print()
#
# clothing_product1 = ClothingProduct("T-shirt", 79.99, 100, "Light Blue cotton T-shirt",
#                            5671362)
# print(clothing_product1.get_total_value())
# clothing_product2 = ClothingProduct("Jeans", 229.90, 33, "Denim man jeans",
#                                     8314670)
#
# print()
#
# warehouse.add_product(food_product1)
# warehouse.add_product(food_product2)
# warehouse.add_product(electronic_product1)
# warehouse.add_product(electronic_product2)
# warehouse.add_product(clothing_product1)
# warehouse.add_product(clothing_product2)
#
# warehouse.print_products()
#
# print()
#
# warehouse.save_products("products.json")
#
# print()
#
# warehouse.remove_product(7569128)
# warehouse.remove_product(8314670)
#
# print()
#
# warehouse.print_products()
#
# print()
#
# warehouse.save_products("products.json")
