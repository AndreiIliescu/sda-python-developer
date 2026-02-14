number = int(input("Enter a number:"))
div = 2
while div < int(number ** (1 / 2)) + 1:
    if number % div == 0:
        print("Numarul nu este prim")
        break
    div += 1
else:
    print("Numar prim")
