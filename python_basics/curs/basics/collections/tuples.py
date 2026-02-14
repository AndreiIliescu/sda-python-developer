empty_tuple = ()
empty_tuple = tuple()


numbers = (1, 2, 3, 4, 5, 6, 7)
print(type(numbers))

numbers = 1, 2, 3, 4, 5, 6, 7
print(type(numbers))
print(numbers.index(1))
print(numbers.count(2))

print(numbers[1])
print(numbers[0:5:2])
