""" Task 2 – Builder
Write a program that will transform the data read from the text file, character by character with the help of Builders,
into characters:

- hexadecimal values;
- capital letters;
- lowercase letters;
- character counter. """

# Clasa abstracta "Buider"
class Builder:
    def build_part(self, element):
        pass

    def get_result(self):
        pass


# Builder concret pentru valori hex
class HexBuilder(Builder):
    def __init__(self):
        self._result_hex_string = ""

    def build_part(self, element):
        self._result_hex_string += f"0x{ord(element):02x} "

    def get_result(self):
        return self._result_hex_string                            # Returnam sirul complet in hex


class UpperBuilder(Builder):
    def __init__(self):
        self._result_upper_string = ""

    def build_part(self, element):
        self._result_upper_string += element.upper()

    def get_result(self):
        return self._result_upper_string                         # Returnam sirul complet cu majuscule


class LowerBuilder(Builder):
    def __init__(self):
        self._result_lower_string = ""

    def build_part(self, element):
        self._result_lower_string += element.lower()

    def get_result(self):
        return self._result_lower_string                        # Returnam sirul complet cu minuscule


# Builder pentru contor de caractere
class CounterBuilder(Builder):
    def __init__(self):
        self._result_counter = 0                                # Initializam contorul cu 0

    def build_part(self, element):
        self._result_counter += 1                               # Incrementam contorul pentru fiecare caracter procesat

    def get_result(self):
        return self._result_counter                             # Returnam numarul total de caractere


class Director:
    def __init__(self, file_name):
        self._file_name = file_name
        self._builder = None

    def construct(self):
        with open(self._file_name) as file:
            for line in file:
                for char in line:
                    self._builder.build_part(char)             # Trimitem caracterul catre "Builder" pentru a fi procesat

    def set_builder(self, builder):
        self._builder = builder                                # Setam builder-ul concret pe care directorul il va folosi

    def get_result(self):
        return self._builder.get_result()


def main():
    director = Director("test2.txt")                          # Cream un obiect "Director" care va citi fisierul "text2.txt"

    # Cream builderii concreti
    hex_builder = HexBuilder()                                # Builder pt. conversia caracterelor in valori hex
    upper_builder = UpperBuilder()                            # Builder pt. conversia caracterelor in majuscule
    lower_builder = LowerBuilder()                            # Builder pt. conversia caracterelor in minuscule
    counter_builder = CounterBuilder()                        # Builder pt. numararea caracterelor

    # Folosim "HexBuilder/UpperBuilder/LowerBuilder/CounterBuilder"
    director.set_builder(hex_builder)
    director.construct()
    print(director.get_result())

    director.set_builder(upper_builder)
    director.construct()
    print(director.get_result())

    director.set_builder(lower_builder)
    director.construct()
    print(director.get_result())

    director.set_builder(counter_builder)
    director.construct()
    print(director.get_result())


if __name__ == "__main__":
    main()

# Functia "main()" deminstreaza pattern-ul "Builder"
# Acelasi "Director" poate construi rezultatul complet diferit, doar schimband "Builder-ul"
# Directorul nu stie cum se construieste rezultatul - doar trimite datele catre "Builder"
