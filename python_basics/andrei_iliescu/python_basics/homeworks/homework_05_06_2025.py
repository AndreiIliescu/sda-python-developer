# 1 - Sa se citeasca de la tastatura un numar reprezentand grade Celsius.
#  Sa se afiseze echivalentul in grade Fahrenheit.
# Convert Celsius (°C) to Fahrenheit (°F) with the formula: °F = (9 / 5 * °C) + 32.
celsius = int(input("What is the current temperature in degrees Celsius? "))
fahrenheit = (9 / 5) * celsius + 32
print(f"The temperature in degrees Fahrenheit is: {fahrenheit}°F.")


# 2 - Sa se citeasca de la tastatura un numar reprezentand grade Fahrenheit.
#  Sa se afiseze echivalentul in grade Celsius.
# Convert Fahrenheit (°F) to Celsius (°C) with the formula: °C = (°F - 32) * 5 / 9.
fahrenheit = int(input("What is the current temperature in degrees Fahrenheit? "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"The temperature in degrees Celsius is: {celsius}°C.")


# 3 - Fiind date 3 valori numerice in variabilele a, b, c, sa se afseze media lor aritmetica.
# Calculate average of three numbers using: (a + b + c) / 3.
a = float(input("Please insert the first number: "))
b = float(input("Please insert the second number: "))
c = float(input("Please insert the third number: "))
average = (a + b + c) / 3
print(f"The average of the three numbers is: {average}.")


# 4 - Fiind data o valoare numerica, sa se afiseze 25% din ea.
# Calculate 25% of a number using: number * 0.25.
number = float(input("Please insert a number: "))
result = number * (25 / 100)
print(f"25% of {number} is: {result}.")


# 5 - Fiind date 3 numere, sa se afiseze daca sunt pitagoreice sau nu.
# Check if any combination of numbers satisfies a^2 + b^2 = c^2.
a = int(input("Insert 1st number: "))
b = int(input("Insert 2nd number: "))
c = int(input("Insert 3rd number: "))

if a**2 + b**2 == c**2:
    print("The triplet is a Pythagorean triple.")
else:
    print("It is not a Pythagorean triple.")
