### while loop
# Rulează un bloc de cod cât timp o condiție este adevărată:
# Exemplu 1:
n = 5
while n > 0:
    print(n)
    n -= 1
print("Liftoff!")


# Exemplu 2: buclă while cu condiție și break:
import random
max_incercari = 5
incercari = 0
while incercari < max_incercari:
    numar = random.randint(1, 10)
    print(f"Încercare {incercari+1}: număr generat = {numar}")
    if numar == 7:
        print("Ai nimerit 7! Gata.")
        break
    incercari += 1
else:
    print("Scuze, nu ați nimerit numărul potrivit.")
