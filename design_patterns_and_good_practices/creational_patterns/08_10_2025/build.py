''' Exemplu care demostreaza pattern-ul Builder
Folosit pentru a separa procesul de constructie a unui obiect complex (o pizza, in cazul de fata)
de reprezentarea finala a acelui obiect '''

class Cook:                                         # Practic asta e "Directorul" - el controleaza procesul pas cu pas
    '''
    Director - manages the creation of the object
    '''

    def __init__(self):
        self._builder = None                        # Retine referinta catre builder-ul curent

    def prepare(self, builder):
        self._builder = builder
        self._builder.prepare_dough()               # Pregateste aluat
        self._builder.add_extras()                  # Adauga ingrediente suplimentare
        self._builder.bake()                        # Coace pizza


# Interfata abstracta pt. crearea produsului tinta
class PizzaBuilder:
    '''
    Builder - abstract interface for creating target objects
    '''

    def __init__(self):
        self.pizza = Pizza()                        # Initializaza produsul ce va fi construit

    def prepare_dough(self):
      pass                                          # Metoda abstracta pt. prepararea aluatului

    def add_extras(self):
      pass                                          # Metoda abstracta pt. adaugarea ingredientelor

    def bake(self):
      pass                                          # Metoda abstracta pt. coacerea pizzei


# Creaza + combina componente specifice pt. pizza Margherita
class MargeritaBuilder(PizzaBuilder):
    '''
    ConcreteBuilder - a specific builder that creates and combines the components of the created object
    '''

    def prepare_dough(self):
      print("Pregatesc aluatul subtire pt. pizza Margherita")

    def add_extras(self):
      print("Adaug sos de rosii si mozzarella")

    def bake(self):
      print("Coc pizza Margherita la 200℃ timp de 10 minute")


# Creaza + combina componente specifice pt. pizza Pepperoni
class PepperoniBuilder(PizzaBuilder):
    def prepare_dough(self):
      print("Pregatesc aluatul pufos pt. pizza Pepperoni")

    def add_extras(self):
      print("Adaug sos de rosii, mozzarella si felii de pepperoni")

    def bake(self):
        print("Coc pizza Pepperoni la 230℃ timp de 12 minute")


# Obiectul complex final (pizza)
class Pizza:
    '''
    the generated complex object
    '''
    pass


def main():
    cook = Cook()                                     # Directorul - controleaza proces de constructie
    # we choose a builder
    baking = PepperoniBuilder()                       # Alegem builder-ul corect (tipul de pizza)
    cook.prepare(baking)                              # Bucatarul pregateste pizza folosind builder-ul ales
    pizza = baking.pizza                              # Obtinem produsul final construit


if __name__ == "__main__":
    main()
