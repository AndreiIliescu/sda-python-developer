### Create ID card ###

# Cerinta: Scriem o functie create_id_card(n: List[int]) -> str
# Primeste o lista de 13 variabile de tip int
# Verificam daca lista are exact 13 elemente, daca nu un mesaj, "Invalid input!"

# Output: un string in formatul "S-YYMM-DD-XXXXXX"
## S = prima cifra din lista;
## YYMM = urmatoarele 4 cifre (an + ziua);
## DD = urmatoarele 2 cifre (ziua);
## XXXXXX = ultimele 6 cifre (cod unic)

### Algoritm:
# 1. Start
# 2. Definim functia si parametrul pe care il primeste (o lista de int-uri) + return-ul, un str.
# 3. Verificam daca lista contine fix 13 elemente
## daca nu -> returnez "Invalid input!"
## daca da:
# 4. Cream o serie de substring-uri + sliceing pe ele pentru a imparti elementele conform formatului dat
## transformam prima cifra: n[0:1]
## transformam urmatoarele patru cifre in grupul "YYMM" (an + luna): n[1:5]
## transformam urmatoarele doua cifre in grupul "DD" (zi): n[5:7]
## transformam ultimele sase cifre grupul "XXXXXX" (cod unic): n[7:14]
# 5. Concatenam substring-urile in formatul specificat
# 6. return string
# 7. End

### Implementarea algoritmului in cod Python
from typing import List


def create_id_card(n: List[int]) -> str:

    if len(n) != 13:
        return "Invalid input!"

    else:
        s = "".join(str(n) for n in n[0:1])
        yymm = "".join(str(n) for n in n[1:5])
        dd = "".join(str(n) for n in n[5:7])
        xxxxxx = "".join(str(n) for n in n[7:14])

        return f"Id card: {s}-{yymm}-{dd}-{xxxxxx}"


id_list = [5, 2, 5, 0, 9, 1, 0, 4, 5, 6, 7, 8, 9]
result = create_id_card(id_list)
print(result)
