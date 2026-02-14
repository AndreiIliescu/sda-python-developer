from functools import reduce


# 1. Scrieti o functie care ia ca paramtru o lista de cuvinte si creeaza o lista noua doar cu prima litera.
# Ex input: ['appla', 'banana', 'cherry']
# output: ['a', 'b', 'c']

fruits = ['appla', 'banana', 'cherry']
first_letter_list = list(map(lambda x: x[0], fruits))
print(first_letter_list, "\n")

# ======================================================================================================================

# 2. Scrieti o functie care elimina numerele mai mici decat zero dintr-o lista de numere.
# Ex input: [1, -1, 5, 6, -3]
# output: [1, 5, 6]

numbers = [1, -1, 5, 6, -3]
no_numbers_less_than_zero = list(filter(lambda x: x > 0, numbers))
print(no_numbers_less_than_zero, "\n")

# ======================================================================================================================

# 3. Scrieti o functie care converteste o lista de strings intr-un singur string
# Ex input: ["Hello", "lambda", "functions", "!"]
# output: "Hello lamba functions !"

main_list = ["Hello", "lambda", "functions", "!"]
one_string = reduce(lambda x, y: x + " " + y, main_list)
print(one_string, "\n")

# ======================================================================================================================

# 4. Scrieti o functie care determina cuvintele palindrom dintr-o lista de cuvinte.
# Un palindrom este un cuvant care se citeste la fel de la stanga la dreapta si invers.
# Ex input: ["rotor", "level", "radar", "mama"]
# output: ["rotor", "level", "radar"]

list_of_words = ["rotor", "level", "radar", "mama"]
palindrome_list = list(filter(lambda x: x == x[::-1], list_of_words))
print(palindrome_list, "\n")

# ======================================================================================================================

# 5. O functie care returneaza cel mai lung cuvant dintr-o lista
# Ex input: ["apple", "banana", "cherry", "kiwi"]
# output: cherry

# return "cherry"
words_list = ["apple", "banana", "cherry", "kiwi"]
longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words_list)
print(longest_word, "\n")

# return "banana"
words_list = ["apple", "banana", "cherry", "kiwi"]
longest_word = reduce(lambda x, y: x if len(x) >= len(y) else y, words_list)
print(longest_word, "\n")
