""" Ofera o interfata pt. a crea 'familii' de obiecte inrudite, fara a specifica clasele concrete.
ex. fabrici de masini cu volan pe stanga si dreapta care produc mai multe tipuri de masini.

'Abstract Factory' extinde pattern-ul 'Factory Method' si adauga un nivel suplimentar de abstractizare.

Exemplul urmator ne arata cum sa construim obiecte care extind interfata clasei 'Car', avem 6 implementari ale
aceleiasi interfete:
- AudiA4Wagon
- AudiA4Sedan
- AudiA4Hatchback
- ToyotaCorollaWagon
- ToyotaCorollaSedan
- ToyotaCorollaHatchback

Primele 3 apartin unui grup (Audi A4) si urmatoarele 3 apartin grupului 'ToyotaCorolla'. """

class Car:
    def get_type(self):
        pass


    def get_model_name(self):
        pass


    def get_cylinders_num(self):
        pass


    def get_producer(self):
        pass


    def get_engine_volume(self):
        pass


    def get_trunk_size(self):
        pass

class AbstractCar(Car):
    def __str__(self):
        return (f"Car: {self.get_producer()} {self.get_model_name()} {self.get_type()} has {self.get_cylinders_num()} "
                f"cylinders and engine {self.get_engine_volume()} and trunk size {self.get_trunk_size()} litres")


# Baza pt. toate Toyota Corolla
class ToyotaCorolla(AbstractCar):
    def get_model_name(self):
        return "Corolla"                           # Numele modelului


    def get_producer(self):
        return "Toyota"                            # Numele producatorului


class ToyotaCorollaWagon(ToyotaCorolla):
    def get_type(self):
        return "Wagon"                             # Tip caroserie


    def get_cylinders_num(self):
        return 4                                   # 4 cilindri


    def get_engine_volume(self):
        return 1.6                                 # motor 1.6l


    def get_trunk_size(self):
        return 540                                 # portbagaj 540 litrii


# Pe baza modelului de mai sus, simular pt. Hatchback si Sedan
class ToyotaCorollaHatchback(ToyotaCorolla):
    def get_type(self):
        return "Hatchback"


    def get_cylinders_num(self):
        return 4


    def get_engine_volume(self):
        return 2.0


    def get_trunk_size(self):
        return 350


class ToyotaCorollaSedan(ToyotaCorolla):
    def get_type(self):
        return "Sedan"


    def get_cylinders_num(self):
        return 4


    def get_engine_volume(self):
        return 1.8


    def get_trunk_size(self):
        return 420


# Ulterior si pt. Audi A4 la fel implementarea
class AudiA4(AbstractCar):
    def get_model_name(self):
        return "A4"


    def get_producer(self):
        return "Audi"


class AudiA4Wagon(AudiA4):
    def get_type(self):
        return "Wagon"


    def get_cylinders_num(self):
        return 4


    def get_engine_volume(self):
        return 1.8


    def get_trunk_size(self):
        return 520


class AudiA4Hatchback(AudiA4):
    def get_type(self):
        return "Hatchback"


    def get_cylinders_num(self):
        return 6


    def get_engine_volume(self):
        return 2.4


    def get_trunk_size(self):
        return 300


class AudiA4Sedan(AudiA4):
    def get_type(self):
        return "Sedan"


    def get_cylinders_num(self):
        return 4


    def get_engine_volume(self):
        return 2.0


    def get_trunk_size(self):
        return 450


# Apoi o interfata comuna pt. toate fabricile:
# 3 metod, una pt. Wagon, una pt. Hatchback si una pt. Sedan
class CarFactory:
    def create_Wagon(self):
        pass                                    # Implementarea efectiva va fi in fabricile concrete


    def create_hatchback(self):
        pass


    def create_sedan(self):
        pass


# Fabrica pt. Toyota Corolla
class ToyotaCorollaFactory(CarFactory):
    def create_Wagon(self):
        return ToyotaCorollaWagon()


    def create_hatchback(self):
        return ToyotaCorollaHatchback()


    def create_sedan(self):
        return ToyotaCorollaSedan()

# Fabrica pt. Audi A4
class AudiA4Factory(CarFactory):
    def create_Wagon(self):
        return AudiA4Wagon()


    def create_hatchback(self):
        return AudiA4Hatchback()


    def create_sedan(self):
        return AudiA4Sedan()


# Clasa care ofera abstractizare suplimentara pt. a selecta fabrica dorita
class FactoryProvider:
    @staticmethod
    def create_factory(factory_type):
        # Daca utilizatorul alege "T", returneaza fabrica Toyota
        if factory_type == 'T':
            return ToyotaCorollaFactory()
        elif factory_type == 'A':
            return AudiA4Factory()
        else:
            return None                                    # Daca nu exista tip valid


# Exemplu de folosire
def main():
    factory_type = input('What car do you want to produce - choose A or T: ')
    factory = FactoryProvider.create_factory(factory_type) # Obtinem fabrica corespunzatoare folosind "FactoryProvider"

    if factory:
        hatchback = factory.create_hatchback()             # Creaza un hatchback
        print(hatchback)


if __name__ == '__main__':
    main()
