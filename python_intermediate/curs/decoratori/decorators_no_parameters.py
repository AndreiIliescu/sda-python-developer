# Exemplu print numele functiei vs apelat functia
# def return_message():
#     return 'hello'
#
# print(return_message)
# print(return_message())
from datetime import datetime


### Decorators with no parameters ###

# Atunci cand folosim aceasta functie cu simbolul @ ca sa decoram o functie
# Parametrul func va fi inlocuit cu functia decorata
def my_decorator(func):
    print('in decorator')

    # 'Inveleste' (wraps) functia originala
    def wrapper(*args, **kwargs):
        print('in wrapper')
        func(*args, **kwargs)

    print('la finalul my_decorator')

    # Returnam functia wrapper
    # !Nu adaugati (), adica wrapper()
    # Vrem sa returnam numele functiei, nu sa o apelam
    return wrapper

# Acest decorator va permite executarea unei functii doar intr-un interval orar
def disable_at_night(func):
    def wrapper(*args, **kwargs):
        # Rulam functia originala doar daca suntem in intervalul orar potrivit
        if 21 <= datetime.now().hour < 22:
            func(*args, **kwargs)

    return wrapper

# Atentie! Daca aveti mai multi decoratori
# Logica din interirul lor se va executa pe rand
# de la primul folosit, la ultimul, pana la functia originala
@disable_at_night
@my_decorator
def say_something(extra):
    print('Hello World!' + extra)

say_something('si cu altele', 'text_extra')
