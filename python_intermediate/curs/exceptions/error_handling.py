# try, except, finally

# Structura
# try:
    # codul pe care incercam sa-l rulam
    # si pe care il suspectam ca ar avea erori
# except Exception:
    # codul se executa daca apare o eroare in try
    # Exception este clasa de baza pentru erori
    # poate fi: AttributeError, IndexError, etc.
# finally:
    # (este optional)
    # codul de aici ruleaza la final, indiferent daca am avut o eroare sau nu

# Exemplul 1
try:
    a = 5
    b = 5 / 1

    assert 4 == 3

    a.append(10)
# Cazul 1: Fiecare exceptie cu proproiul bloc de cod
# except ZeroDivisionError:
#     print("Impartit la zero")
# except AssertionError:
#     print("error la assert")
# except AttributeError:
#     print("Int nu are append")
# Cazul 2: Daca avem un except care cuprinde mai multe erori (doar una dintre paranteze sa se intample)
except(ZeroDivisionError, AssertionError):
    print("Zero div, sau assertion")
except AttributeError:
    print("Attr error")

finally:
    print("Am ajuns la final")


# Exemplul 2
# Except Exception -> cazul general care cuprinde toate erorile
try:
    f = open("file.txt")
    print(f.read())
except Exception:
    print("Eroare la deschiderea fisierului")


# Exemplul 3
x = 5
my_list = [1, 0, 2]

for elem in my_list:
    try:
        result = x / elem
    except ZeroDivisionError:
        print("Nu poti imparti la 0.")

        # In cazul unei erori, trecem mai departe in for
        # (sarim peste eroare)
        continue

    print(f"Result is {result}")
