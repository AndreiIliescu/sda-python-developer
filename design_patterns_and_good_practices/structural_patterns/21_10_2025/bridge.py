""" BRIDGE

Separa o abstractie de implementarea ei.
Scop: ca sa poata ambele sa evoalueze independent.
Se foloseste cand vrei sa ai o flexibilitate. """

# ex.
class Drink:
    def get_volume(self):
        pass

    def is_addictive(self):
        pass

    def get_number_of_sugar_lumps(self):
        pass

    def get_taste(self):
        pass


class Coffee(Drink):
    def get_volume(self):
        return "150ml"

    def is_addictive(self):
        return True

    def get_number_of_sugar_lumps(self):
        return 0

    def get_taste(self):
        return "bitter"


class Tea(Drink):
    def get_volume(self):
        return "250ml"

    def is_addictive(self):
        return False

    def get_number_of_sugar_lumps(self):
        return 2

    def get_taste(self):
        return "sweet"


class DrinkPurchase:
    def buy(self, cost):
        pass


class CoffeePurchase(DrinkPurchase):
    def buy(self, cost):
        print(f"Buying a coffee for {cost}")
        return Coffee()


class TeaPurchase(DrinkPurchase):
    def buy(self, cost):
        print(f"Buying a tea for {cost}")
        return Tea()
