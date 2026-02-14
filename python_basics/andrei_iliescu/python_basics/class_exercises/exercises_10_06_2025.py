# 1 - Sa se scrie cate un convertor de temperatura, cu valori citite de la tastatura:
# Kelvin -> Celsius
kelvin = float(input("Enter temperature in degree Kelvin: "))
celsius = kelvin - 273.15
print(f"The temperature in degree Celsius is: {celsius}°C.")

# Celsius -> Kelvin
celsius = float(input("Enter temperature in degree Celsius: "))
kelvin = celsius + 273.15
print(f"The temperature in degree Kelvin is: {kelvin}°K.")

# Fahrenheit -> Kelvin
fahrenheit = float(input("Enter temperature in degree Fahrenheit: "))
kelvin = (fahrenheit - 32) * 5/9 + 273.15
print(f"The temperature in degree Kelvin is: {kelvin}°K.")

# Kelvin -> Fahrenheit
kelvin = float(input("Enter temperature in degree Kelvin: "))
fahrenheit = (kelvin - 273.15) * 9/5 + 32
print(f"The temperature in degree Fahrenheit is: {fahrenheit}°F.")


# 2 - Fiind date 3 numere citite de la tastaura, sa se calculeze media lor armonica.
# Harmonic mean
a = float(input("Please insert the first number: "))
b = float(input("Please insert the second number: "))
c = float(input("Please insert the third number: "))
harmonic_mean = (2 * a * b) / (a + b)
print(harmonic_mean)


# 3 - Fiind date 3 valori si 3 ponderi cititie de la tastatura, sa se afiseze media lor ponderata.
# Weighted arithmetic mean
a1 = float(input("Insert the first value: "))
p1 = float(input("Insert the first value: "))
b2 = float(input("Insert the second value: "))
p2 = float(input("Insert the second value: "))
c3 = float(input("Insert the third value: "))
p3 = float(input("Insert the third value: "))
weighted_arithmetic_mean = (a1 * p1 + b2 * p2 + c3 * p3) / (p1 + p2 + p3)
print(f"Weighted arithmetic mean is: {weighted_arithmetic_mean}")


# 4 - Fiind dat un text citit de la tastaura, sa se afiseze tot al 2-lea caracter.
# Displays the 2nd character of a text read from the keyboard
text = input("Insert text: ")
solution = text[1::2]
print(solution)


# 5 - Fiind dat un text citit de la tastatura, sa se afiseze in ordine inversa.
# Displays text read from the keyboard in reverse order
user_input = input("Enter a text: ")
reversed_input = user_input[::-1]
print(reversed_input)


# 6 - Fiind citite de la tastatura minumul de valori necesare, sa se calculaze:
#  Aria, Perimetru pentru: Cerc, Triunghi, Patrat, Dreptunghi.
#  Volumul pentu: cub, piramida, sfera, con, trunchi de con.
# Area of the circle
pi = 3.14
r = float(input("Enter circle radius: "))
d = 2 * r
circle_area = pi * r ** 2
print(circle_area)

# Perimeter of the circle
circle_circumference = 2 * pi * r
print(circle_circumference)

# Area of the triangle
x = float(input("Enter value for the side pf triangle: "))
h = float(input("Enter value for height of triangle: "))
area_triangle = (x * h) / 2
print(area_triangle)

# Perimeter of the triangle
perimeter_triangle = 3 * x
print(perimeter_triangle)

# Area of the square
l = float(input("Insert the length of one side of the square: "))
square_area = l ** 2
print(square_area)

# Perimeter of the square
square_perimeter = l * 4
print(square_perimeter)

# Area of the rectangle
length = float(input("Insert the length: "))
width = float(input("Insert the width: "))
area_of_rectangle = length * width
print(area_of_rectangle)

# Perimeter of rectangle
perimeter_of_rectangle = 2 * length + 2 * width
print(perimeter_of_rectangle)

# Volume of cube
side_length = float(input("Insert the length of one side of the cube: "))
cube_volume = side_length ** 3
print(cube_volume)

# Volume of pyramid
l = float(input("Insert the value for the side of the pyramid: "))
base_area = l ** 2
height = float(input("Insert the height of the pyramid: "))
volume_of_pyramid = (1 / 3) * base_area * height
print(volume_of_pyramid)

# Volume of sphere
radius_of_sphere = float(input("Insert the radius the sphere: "))
sphere_volume = (4 * pi * radius_of_sphere ** 3) / 3
print(sphere_volume)

# Volume of cone
radius_of_cone = float(input("Insert the radius the cone: "))
height_of_cone = float(input("Insert the height the cone: "))
volume_of_cone = 1 / 3 * (pi * radius_of_cone ** 2 * height_of_cone)

# Volume of truncated cone
radius_bottom = float(input("Insert the radius of the larger base of the truncated cone: "))
radius_top = float(input("Insert the radius of the smaller base of the truncated cone: "))
height = float(input("Insert the height of the truncated cone: "))
volume_of_truncated_cone = (1 / 3) * pi * (radius_bottom**2 + radius_bottom * radius_top + radius_top**2) * height
print(volume_of_truncated_cone)


# 7 - Sa se rezolve ecuatia de grad 1: a*x+b=0
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
if a == 0:
    print("No solution: a cannot be zero.")
else:
    x = -b / a
    print(f"The solution is x = {x}")


# 8 - Sa se rezolve ecuatia de grad 2: a*x**2+b*x+c=0



# 9 - Sa se scrie un convertor de valori metrice->imperiale pentru distanta, greutate
# Distance
meters = float(input("Insert the value for meters: "))
feet = meters * 3.28
print(f"Feet: {feet}")

kilometers = float(input("Insert the value for kilometers: "))
miles = kilometers * 0.62
print(f"Miles: {miles}")

# Weight
kilograms = float(input("Insert the value for kilograms: "))
pounds = kilograms * 2.20
print(f"Pounds: {pounds}")


# 10 - Sa se scrie un convertor de valori imperiale->metrice pentru distanta, greutate
# Weight
pounds = float(input("Insert the value for pounds: "))
kg = pounds / 2.20
print(f"Kilograms: {kg}")

# Distance
feet = float(input("Insert the value for feet: "))
m = feet / 3.28
print(f"Meters: {m}")

miles = float(input("Insert value for miles: "))
km = miles / 0.62
print(f"Kilometers: {km}")
