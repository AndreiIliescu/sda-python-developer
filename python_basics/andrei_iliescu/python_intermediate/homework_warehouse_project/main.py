from warehouse import Warehouse


if __name__ == "__main__":
    w = Warehouse("Main Warehouse")
    w.load_products()
    # w.load_reservation()

    the_program_is_running = True

    while the_program_is_running:
        w.print_products()

        print("/=== MENU ===/\n"
              "1. Add a new food product\n"
              "2. Add a new electronic product\n"
              "3. Add a new clothing product\n"
              "4. Update infos about a product\n"
              "5. Remove all expired products\n"
              "6. Remove all out of warranty products\n"
              "7. Delete any product by their bar code\n"
              "8. Add discount to a product\n"
              "9. Reserve a product now, buy it later\n"
              "10. Buy a product\n"
              "11. Exit program\n")

        user_choice = input("Choose an option from the menu: ")

        match user_choice:
            case "1":
                w.add_food_product()
            case "2":
                w.add_electronic_product()
            case "3":
                w.add_clothing_product()
            case "4":
                w.update_product()
            case "5":
                w.remove_expired_products()
            case "6":
                w.remove_out_of_warranty_products()
            case "7":
                w.delete_product()
            case "8":
                w.add_discount()
            case "9":
                w.reserve_product()
            case "10":
                w.buy_product()
            case "11":
                the_program_is_running = False
            case _:
                print("This is an invalid option. "
                      "Try again and make sure you chose one of the options from the menu!\n")

    w.save_products()
    # w.save_reservation()

    print("Thank you for stopping by. See you later!")
