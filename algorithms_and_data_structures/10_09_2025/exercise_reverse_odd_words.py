### Revers odd words ###

# Cerinta: Inversarea cuvintelor pare.
# Scrie o functie reverse_odd_words(string: str) -> str:
## primeste un sir de caractere format din mai multe cuvinte, separate prin spatiu;
## toate cuvintele de pe pozitii pare (indexul de la 0) se returneaza exact cum sunt;
## toate cuvintele de pe pozitii impare se returneaza inversate.

## ex.: Input: "Python is super fun" -> Output: "Python si super nuf".
## Pentru a imparti sirul de cuvinte (string-ul initial) se foloseste metoda "split()".

### Algoritm:
# 1. Start
# 2. Impartim string-ul in lista de cuvinte folosind "split()"
# 3. Initializam o variabila, "new_string" goala, pentru rezultatul final
# 4. Parcurgem lista de cuvinte
# 5. Verificam daca indexul este par sau impar:
## daca este par: pastram cuvantul asa cum este;
## daca este impar: inversam cuvantul "[::-1]".
# 6. Adaugam cuvantul in "new_string" si un spatiu dupa fiecare cuvant
# 7. Returnam "new_string"
# 8. End

### Implementarea algoritmului in cod Python
def reverse_odd_words(string: str) -> str:
    words = string.split()
    new_string = ""

    for i, word in enumerate(words):
        if i % 2 == 0:
            new_string += word
        else:
            new_string += word[::-1]
        new_string += " "

    return new_string


print(reverse_odd_words("Python is super fun"))

# Aceeasi abordare, doar ca folosind list comprehension.
# De fapt am folosit acelasi algoritm prezentat mai sus
def reverse_odd_words_2(string: str) -> str:
    words = string.split()
    result = [word if i % 2 == 0 else word[::-1] for i, word in enumerate(words)]
    return " ".join(result)


print(reverse_odd_words_2("Python is super fun"))
