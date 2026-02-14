import datetime
import pickle
from decorators import execute_only_at_night_time, loading
from products import FoodProduct, ElectronicProduct, ClothingProduct


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.products = []
        # self.reserved_products = []

    @execute_only_at_night_time
    def add_food_product(self):
        print("/=== Enter the details to add a new food product ===/")
        product_name = input("Enter product name: ")
        product_price = float(input("Enter product price: "))
        product_quantity = int(input("Enter product quantity: "))
        product_description = input("Enter product description: ")
        product_expiration_date = datetime.datetime.strptime(
            input("Enter product expiration date (YYYY-MM-DD): "), "%Y-%m-%d").date()
        product = FoodProduct(product_name, product_price, product_quantity, product_description,
                              product_expiration_date)
        self.products.append(product)
        print("/=== New food product successfully added! ===/\n")

    @execute_only_at_night_time
    def add_electronic_product(self):
        print("/=== Enter the details to add a new electronic product ===/")
        product_name = input("Enter product name: ")
        product_price = float(input("Enter product price: "))
        product_quantity = int(input("Enter product quantity: "))
        product_description = input("Enter product description: ")
        product_warranty_date = datetime.datetime.strptime(input("Enter product warranty date (YYYY-MM-DD): "),
                                                           "%Y-%m-%d").date()
        product = ElectronicProduct(product_name, product_price, product_quantity, product_description,
                                    product_warranty_date)
        self.products.append(product)
        print("/=== New electronic product successfully added! ===/\n")

    @execute_only_at_night_time
    def add_clothing_product(self):
        print("/=== Enter the details to add a new clothing product ===/")
        product_name = input("Enter product name: ")
        product_price = float(input("Enter product price: "))
        product_quantity = int(input("Enter product quantity: "))
        product_description = input("Enter product description: ")
        product_color = input("Enter product color: ")
        product_size = input("Enter product size: ")
        product_material = input("Enter product material: ")
        product = ClothingProduct(product_name, product_price, product_quantity, product_description, product_color,
                                  product_size, product_material)
        self.products.append(product)
        print("/=== New clothing product successfully added! ===/\n")

    @execute_only_at_night_time
    def update_product(self, bar_code, new_price=None, new_quantity=None):
        product_to_update = next(filter(lambda p: p.bar_code == bar_code, self.products), None)
        if product_to_update:
            if new_price is not None:
                product_to_update.price = new_price
            if new_quantity is not None:
                product_to_update.quantity = new_quantity
            self.save_products()
            print(f"/=== Product {product_to_update.name} updated successfully ===/\n")
        else:
            print("/=== No product found with that bar code ===/\n")

    @loading(total_seconds=5)
    def save_products(self):
        with open("warehouse_products.pickle", "wb") as data_file:
            pickle.dump(self.products, data_file)
        print(f"/=== Products successfully saved to {'warehouse_products'}! ===/\n")

    @loading(total_seconds=5)
    def print_products(self):
        if not self.products:
            print("/=== There are no products in the Main Warehouse ===/\n")
            return
        for product in self.products:
            if isinstance(product, FoodProduct):
                print(f"/{'='*58} Food Products {'='*59}/")
                print("-"*134)
                print(f"{'Name':15} | {'Price':10} | {'Quantity':10} | {'Description':28} | {'Bar Code':36} | "
                      f"{'Expiration date':18} |")
                print("-"*134)
                print(f"{product.name:15} | {product.price:10} | {product.quantity:10} | {product.description:25} | "
                      f"{product.bar_code:35} | {product.expiration_date}")
                print("-"*134, "\n")
            elif isinstance(product, ElectronicProduct):
                print(f"/{'='*55} Electronic Products {'='*56}/")
                print("-"*134)
                print(f"{'Name':18} | {'Price':10} | {'Quantity':10} | {'Description':28} | {'Bar Code':36} | "
                      f"{'Warranty date':15} |")
                print("-"*134)
                print(f"{product.name:15} | {product.price:10} | {product.quantity:10} | {product.description:28} | "
                      f"{product.bar_code:36} | {product.warranty_date}")
                print("-"*134, "\n")
            elif isinstance(product, ClothingProduct):
                print(f"/{'='*70} Clothing Products {'='*70}/")
                print("-"*161)
                print(f"{'Name':15} | {'Price':10} | {'Quantity':10} | {'Description':28} | {'Bar Code':36} | "
                      f"{'Color':15} | {'Size':7} | {'Material':17} |")
                print("-"*161)
                print(f"{product.name:15} | {product.price:10} | {product.quantity:10} | {product.description:28} | "
                      f"{product.bar_code:36} | {product.color:15} | {product.size:7} | {product.material:17} |")
                print("-"*161, "\n")

    @loading(total_seconds=5)
    def load_products(self):
        try:
            with open("warehouse_products.pickle", "rb") as data_file:
                self.products = pickle.load(data_file)
            print(f"/=== Products successfully loaded from {'warehouse_products'}! ===/\n")
        except Exception:
            print("/=== Something went wrong! The file cannot be loaded. ===/\n")

    @execute_only_at_night_time
    def remove_expired_products(self):
        expired_products = list(filter(lambda p: isinstance(p, FoodProduct) and p.is_expired(), self.products))
        for p in expired_products:
            print(f"/=== The {p.name} has been removed from the Main Warehouse ===/\n")
        self.products = [p for p in self.products if not (isinstance(p, FoodProduct) and p.is_expired())]
        if not expired_products:
            print("/=== There are no expired products to be removed ===/\n")

    @execute_only_at_night_time
    def remove_out_of_warranty_products(self):
        out_of_warranty = list(filter(lambda p: isinstance(p, ElectronicProduct) and not p.is_under_warranty(),
                                      self.products))
        for p in out_of_warranty:
            print(f"/=== The {p.name} has been removed from the Main Warehouse ===/\n")
        self.products = [p for p in self.products if not (isinstance(p, ElectronicProduct) and not p.is_under_warranty())]
        if not out_of_warranty:
            print("/=== There are no out of warranty products to be removed ===/\n")

    @execute_only_at_night_time
    def delete_product(self):
        bar_code_input = input("Please enter the bar code of the product you want to delete: ")
        product_to_delete = next(filter(lambda p: p.bar_code == bar_code_input, self.products), None)
        if product_to_delete:
            self.products.remove(product_to_delete)
            print(f"/=== Product {product_to_delete.name} has been successfully deleted ===/\n")
        else:
            print("/=== No product found with that bar code! ===/\n")

    @execute_only_at_night_time
    def add_discount(self, bar_code, discount_percent):
        product = next(filter(lambda p: p.bar_code == bar_code, self.products), None)
        if product:
            product.price = product.price * (1 - discount_percent / 100)
            self.save_products()
            print(f"/=== Discount of {discount_percent}% applied to {product.name}. New price: {product.price} ===/\n")
        else:
            print("/=== No product found with that bar code ===/\n")

    def reserve_product(self):
        print("/=== [Not yet implemented. COMIN SOON!] ===/\n")

    def save_reservation(self):
        pass

    def load_reservation(self):
        pass

    def buy_product(self):
        product_name_input = input("Please enter the product name: ")
        found_product = next(filter(lambda p: p.name == product_name_input, self.products), None)
        if not found_product:
            print("No product found with this name\n")
            return
        product_quantity_input = int(input("Please enter the quantity you want to buy: "))
        total_amount_to_pay = product_quantity_input * found_product.price
        found_product.quantity -= product_quantity_input
        print(f"/=== You have successfully bought {product_quantity_input} {found_product.name}. "
              f"Total to pay: {total_amount_to_pay} ===/\n")
