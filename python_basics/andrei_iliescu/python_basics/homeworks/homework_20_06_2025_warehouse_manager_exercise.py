import pickle
import os.path
from datetime import datetime
from homework_24_06_2025_warehouse_manager_classes_exercises import Product

W_NAME = 42
W_QUANTITY = 10
W_PRICE = 10
W_CODE = 12

NAME = "Name"
QUANTITY = "Quantity"
DESCRIPTION = "Description"
CODE = "Unique_Code"
PRICE = "Price"


def show_products(products):
    header = [NAME, QUANTITY, PRICE, CODE]
    print(f"┌{"─" * W_NAME}┬{"─" * W_QUANTITY}┬{"─" * W_PRICE}┬{"─" * W_CODE}┐")
    print(f"|{header[0]:{W_NAME}}│{header[1]:{W_QUANTITY}}│{header[2]:{W_PRICE}}│{header[3]:{W_CODE}}│")
    print(f"├{"─" * W_NAME}┼{"─" * W_QUANTITY}┼{"─" * W_PRICE}┼{"─" * W_CODE}┤")
    for product in products:
        print(f"│{product.name:{W_NAME}}│{product.quantity:{W_QUANTITY}}│{product.price:{W_PRICE}}│"
              f"{product.unique_code:{W_CODE}}│")
    print(f"└{"─" * W_NAME}┴{"─" * W_QUANTITY}┴{"─" * W_PRICE}┴{"─" * W_CODE}┘")
    print()


def save_products(products):
    with open("products.pickle", "wb") as file:
        pickle.dump(products, file)


def load_products():
    if os.path.exists("products.pickle"):
        with open("products.pickle", "rb") as file:
            return pickle.load(file)
    else:
        return [
            Product("Tablet", 2300.99, 3, "Samsung Galaxy Tab S10+", 46351),
            Product("Laptop", 9660.89, 13, "Asus ROG Scar 18", 56577),
            Product("Mobile", 3500.45, 10, "Iphone 13 Pro Max", 7566445),
            Product("Smartwatch", 750.50, 8, "Lenovo GT3", 165162),
        ]


def add_products(products: list):
    name_input = input("Name: ")
    quantity_input = input("Quantity: ")
    price_input = input("Price: ")
    code_input = input("Code: ")
    description_input = input("Description: ")

    products.append(Product(name_input, float(price_input), int(quantity_input), description_input, int(code_input)))
    save_products(products)


def buy_product(products):
    product_name = input("Enter the product you want to buy: ").strip().lower()
    for item in products:
        if item.name.lower() == product_name:
            if item.quantity > 0:
                item.quantity -= 1
                print(f"You bought one {item.name}.")
                print(f"Remaining quantity: {item.quantity}")
                print(f"New total price for {item.name}: {item.quantity * item.price:.2f}")
            else:
                print(f"Sorry, {item.name} is out of stock.")
            break
    else:
        print("Product not found in cart.")
    save_products(products)


def update_product(products):
    code = int(input("Enter the product code to update: "))
    for product in products:
        if product.unique_code == code:
            print("Leave field empty to skip update.")
            new_name = input(f"New name ({product.name}): ")
            new_price = input(f"New price ({product.price}): ")
            new_quantity = input(f"New quantity ({product.quantity}): ")
            new_description = input(f"New description ({product.description}): ")

            if new_name:
                product.name = new_name
            if new_price:
                product.price = float(new_price)
            if new_quantity:
                product.quantity = int(new_quantity)
            if new_description:
                product.description = new_description

            print("Product updated successfully.")
            save_products(products)
            return
    print("Product not found.")


def delete_product(products):
    code = int(input("Enter the product code to delete: "))
    for product in products:
        if product.unique_code == code:
            products.remove(product)
            print(f"Product '{product.name}' deleted successfully.")
            save_products(products)
            return
    print("Product not found.")


def apply_discount(products):
    code = int(input("Enter the product code for discount: "))
    percent = float(input("Enter discount percentage (0-100): "))
    for product in products:
        if product.unique_code == code:
            discount_amount = product.price * percent / 100
            product.price -= discount_amount
            print(f"Discount applied. New price: {product.price:.2f}")
            save_products(products)
            return
    print("Product not found.")


def reserve_product(products):
    code = int(input("Enter the product code to reserve: "))
    quantity = int(input("Enter quantity to reserve: "))
    date_str = input("Enter reservation date (DD-MM-YYYY): ")
    time_str = input("Enter reservation time (HH:MM): ")
    reservation_dt = datetime.strptime(f"{date_str} {time_str}", "%d-%m-%Y %H:%M")

    for product in products:
        if product.unique_code == code:
            if product.quantity >= quantity:
                product.quantity -= quantity
                print(f"Reservation confirmed for {quantity} x {product.name} on {reservation_dt}.")
                save_products(products)
                return
            else:
                print(f"Only {product.quantity} items available.")
                return
    print("Product not found.")


class Main:
    def __init__(self):
        self.products = load_products()

    def menu(self):
        while True:
            print("""
1. Show Products
2. Add Product
3. Buy Product
4. Update Product
5. Delete Product
6. Apply Discount
7. Reserve Product
0. Exit
""")
            choice = input("Choose option: ")
            if choice == "1":
                show_products(self.products)
            elif choice == "2":
                add_products(self.products)
            elif choice == "3":
                buy_product(self.products)
            elif choice == "4":
                update_product(self.products)
            elif choice == "5":
                delete_product(self.products)
            elif choice == "6":
                apply_discount(self.products)
            elif choice == "7":
                reserve_product(self.products)
            elif choice == "0":
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    Main().menu()
