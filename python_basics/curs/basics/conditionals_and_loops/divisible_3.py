for i in range (1, 51):
    print(3 * i)

for number in range (3, 3 * 50 + 1, 3):
    print(number)

number = 3  # numer incepe de la 3 si creste cu 3 la fiecare pas
total = 0 #  numara cate numere au fost afisate pana la etc....

while total < 50:
    print(number)
    number += 3
    total += 1
