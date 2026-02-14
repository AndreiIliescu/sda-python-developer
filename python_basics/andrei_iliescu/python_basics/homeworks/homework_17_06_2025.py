# 1 - Fiind dat un text citit de la tastartura,
# sa se scrie un algoritm care numara cate aparitii are fiecare litera din el
text_input = input("Enter some text: ").lower()
letter_count = ""

for letter in text_input:
    if letter.isalpha():
        if letter not in letter_count:
            letter_count += letter

for letter in letter_count:
    print(f"{letter}: {text_input.count(letter)}")


# 2 - sa se scrie un algoritm care afiseaza primele 500 numere prime
prime_numbers = []
number = 2

while len(prime_numbers) < 500:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers.append(number)
    number += 1
print(prime_numbers)


# 3 - Sa se scrie un algoritm care genereaza primele 100 numere ale sirului Fobonacci
a = 0
b = 1
for _ in range(100):
    print(a, end=" ")
    a, b = b, a + b
