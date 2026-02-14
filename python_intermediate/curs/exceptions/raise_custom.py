# Cuvantul raise va "ridica" o eroare
# Eroarea poate opri programul sau poate fi "handled" intr-un try/except
# Sintaxa:
# raise ValueError("Mesajul erorii")

# raise ValueError("Mesajul erorii")

# Exemplu simplu pentru folosirea lui raise
# def my_func(my_list):
#     x = 3
#     for elem in my_list:
#         if elem == 0:
#             raise ValueError("Atentie! Un element din lista este egal cu 0.")
#
#         result = x / elem
#         print(f"Resut is {result}")
#
#
# try:
#     my_func([1, 0, 2])
# except ValueError:
#     print("Un element din lista este egal cu 0.")


# Pentru a crea tipuri noi de erori
# Varianta 1
class CustomException(Exception):
    pass


# raise CustomException

# Varianta 2
class EvenDivisionException(Exception):
    def __init__(self):
        message = "Nu poti imparti cu un nr. par"
        super().__init__(message)


# raise EvenDivisionException


def my_func_even_division(my_list):
    x = 16

    for elem in my_list:
        if elem == 0:
            raise ValueError("Atentie! Un element din lista este egal cu 0.")

        if elem % 2 == 0:
            raise EvenDivisionException

        result = x / elem
        print(f"Result is {result}")


my_func_even_division([1, 3, 2])
