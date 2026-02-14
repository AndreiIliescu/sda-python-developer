empty_list = []
empty_list = list()

numbers = [1, 2, 3, 4, 5, 6, 7]
print(type(numbers))

print(numbers.index(1))
print(numbers.count(2))

print(numbers[1])
print(numbers[0:5:2])

# numbers.append([66, 77, 88])
numbers.append(8)
print(numbers)

numbers.extend([9, 10, 11])
print(numbers)

numbers.insert(1, 12)
print(numbers)

index = numbers.index(12)
numbers[index] = 13
print(numbers)

numbers += [33, 44, 55, 10, 10]
print(numbers)

numbers.pop(0)
print(numbers)

while 10 in numbers:
    numbers.remove(10)
    print(numbers)
