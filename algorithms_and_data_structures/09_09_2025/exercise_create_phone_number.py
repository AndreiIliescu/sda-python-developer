### Phone number ###

# Cerinta: Scrie o functie care primeste de liste de 11 numere ("int") si returneaza un sir de caractere ce reprezinta
# un nr. de tel. intr-un format specific.

# Input: O lista de 11 variabile int.
# Output: Un string formatat.
## ex.: "(+12) 345-678-901".
# primele doua cifre devin prefixul international (+12).
# urmatoarele 3 cifre (345).
# urmatoarele 3 cifre (678).
# si ultimele 3 cifre (901).

### Algoritm
# 1. Start
# 2. Definim functia si parametrii ei + tipuri de date output (str)
# 3. Creare substring-uri pentru fiecare grup de cifre
## transformam primele doua cifre in prefix international n[0:2];
## transformam urmatoarele trei cifre in primul grup n[2:5];
## transformam urmatoarele trei cifre in al doilea grup n[5:8];
## transformam urmatoarele trei cifre in ultimul grup n[8:11].
# 4. Convertim cifrele in string
# 5. Concatenam si formatam a sablonului cerut
# 6. Functia returneaza un string
# 7. End

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1] #11 elemente -> index de la 0 la n-1 (11-1) -> index de la 0 la 10.
# "(+12) 345-678-901".

### Implementarea algoritmului in cod Python
from typing import List

# ".join" este o metoda a string-urilor care uneste toate elementele unui iterabil intr-un singur string.
# foloseste stringul pe care il are ca separator.
# sintaxa: separator.join(iterabil).
def create_phone_number(n: List[int]) -> str:
    str1 = "".join(str(x) for x in n[0:2]) # n[0:2] slicing si ia doar index 0 si 1, apoi ele se convertesc in str.
    str2 = "".join(str(x) for x in n[2:5])
    str3 = "".join(str(x) for x in n[5:8])
    str4 = "".join(str(x) for x in n[8:11])

    return f"(+{str1}) {str2}-{str3}-{str4}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]))
