# verificam daca numarul este de tip int
# daca este int facem verificarile corespunzatoare: daca e par sau impar
# returnam mesajul daca este par sau impar
# daca nu este int => mesaj eroare

def odd_even(number):
    if not isinstance(number, int):
        return 'Error - number must be integer!'
    if number % 2 == 0:
        return 'The number is even!'
    return 'The number is odd!'
