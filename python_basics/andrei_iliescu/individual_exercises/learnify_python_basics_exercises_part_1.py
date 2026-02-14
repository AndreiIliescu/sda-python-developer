"""PART 1"""
'''PYTHON INTRODUCTION EXERCISES'''
# 1 - If you have not done it yet, try to write and run the “Hello, World!”
#  program in one of the Integrated Development Environments (IDE).
#  In Appendix A you will find instructions on how to install and run the PyCharm integrated development environment
print("Hello, World!")

# 2 - Write a program that displays “Hello, !” on the screen (instead of “”, enter your name).
print("Hello, Andrei!")

# 3 - Remove one of the quotation marks around the ‘Hello, World’ text. Try to run the program.
#  Read the message describing the error that has occurred. Then correct the quotes and try to spoil the program
#  in a different way (each time read the description of the error encountered),
#  e.g.:- remove or add a bracket - remove one of the letters in the word “print”
'''printHello, World!")'''

# 4 - Before executing the following lines of the code, try to guess what the result will be:
print("What a beautiful day")
print("What", "a" "beautiful", "day")
print(3)
print(3, 4, 5)
print("1", "2", 3, 4, 5)
print("What", "a" "beautiful", "day", sep=",")

# 5 - Write a code line starting with #. Executing such a code line will not cause any action.
#  In Python, the # character is used to comment on the line. When the Python interpreter encounters the # character,
#  it goes to the next line of the code. Therefore, this character is used to enter comments in the code.
#  Comments will be useful for other programmers who read your code, or for yourself.
# import this
for i in range(8):
    j = 1 << i
    print(f"{j} bytes = {j*8} bits which has {256**j-1} possible values.")

'''DATA TYPES EXERCISES'''
# 1 - Determine the type of the following literals (values):
print(type("Hello"))
print(type(2))
print(type(2.))
print(type(2.0))
print(type("2"))
print(type(4.55))
print(type(-4.3))
print(type(54 + 5j))
print(type(True))
print(type(None))

# 2 - Determine the type of the following expression results:
print(type(2 + 2))
print(type(2 + 2.))
print(type(4 / 2))
print(type(4 / 3))
print(type(4))
print(type(3 * "a"))

# 3 - Calculate the arithmetic mean of any five numbers.
a = 5
b = 6.1
c = 21
d = 8.7
e = 5.29
average = (a + b + c + d + e) / 5
print(average)

# 4 - Calculate the following expressions:
print(3 + 45 - 2.5 * 4)
print(2 ** 3)
print(3.5 * (3-2))
print(501.0 - 99.9999)
print(10.0 / 4.0)
print(10.0 // 4.0)
print(5 % 2)
print(2 == 2)
print(1 != 1)
print(99 > 1.1)
print(True or False)
print(2 == 2 or 1 != 1)
print(True and True and False)
print(2 == 2 and 99 > 1.1 and 1 != 1)
print(not False)
print(not 1 != 1)

# 5 - Correct the logical expressions so that each expression returns the True value.
print("asd" != "qwe")
print(not 3>6)
print("As" <= "ad")
print("Z" < "n")
print(45 == 45)

# 6 - Perform the casting as follows:
#  ◦ cast the following values to the integer type:
print(int(15.5))
print(int(4.01))
print(int(4.99))
print(int(-4.01))
print(int(-4.99))
#  ◦ cast the following numbers to the floating point type:
print(float(0))
print(float(100))
print(float(-4))
#  ◦ cast the following numbers to the boolean type:
print(bool(2))
print(bool(-6.1))
print(bool('a'))
print(bool("abc"))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(''))

'''VARIABLES EXERCISES'''
# 1 - Create variables belonging to the following types: ◦ integer ◦ floating point ◦ string ◦ bool
a = 10
print(type(a))
b = 5.5
print(type(b))
name = "Andrei"
print(type(name))
boolean = True
print(type(boolean))

# 2 - Create the person_age variable and assign an integer type value to it.
#  Display the value and type of the age_person variable on the screen
person_age = 24
print(person_age)
print(type(person_age))

# 3 - Cast the floating point variable with the value of 4.3 into the integer type.
#  Cast the string type variable with the value of “45” into the integer type.
a = 4.3
print(type(int(a)))
b = "45"
print(type(int(b)))

# 4 - Write a program that displays the string “Hello, ! on the screen.
#  Make your name stored in a string type variable..
print("Hello, !")
name = "Andrei"
print("Hello, " + name + "!")

# 5 - Declare two variables corresponding to the sides of the rectangle and count its area and perimeter.
#  Formula for: ◦ area of a rectangle: P = a * b ◦ perimeter of a rectangle: L = 2a + 2b
a = 10
b = 20
area_of_rectangle = a * b
print(area_of_rectangle)
perimeter_of_rectangle = 2 * a + 2 * b
print(perimeter_of_rectangle)

# 6 - Declare the variable corresponding to the diameter of the circle and calculate its area and circumference.
#  The relevant formulas are as follows: ◦ circle area P = pi * r^2 ◦ circle circumference L = 2 * pi * r
#  ◦ Assume 3.14 as the value of pi.
pi = 3.14
r = 10
d = 2 * r
circle_area = pi * r ** 2
print(circle_area)
circle_circumference = 2 * pi * r # or use formula pi * d
print(circle_circumference)

'''CONDITIONS EXERCISES'''
# 1 - Write a program that will display on the screen whether the value of the variable is divisible by 7
number = int(input("Insert a number: "))
if number % 7 == 0:
    print("Divisible by 7.")
else:
    print("Not divisible by 7.")

# 2 - Write a program that will display the text
#  “The value of the variable is odd” on the screen if the value of the variable is odd,
#  and otherwise display the text “The specified value is even”.
number = int(input("Chose a number: "))
if number % 2 == 0:
    print("The specified value is even")
else:
    print("The value of the variable is odd")

# 3 - Write a program that will display on the screen whether the variable value is divisible by 7, by 5 or by 3.
#  If the variable value is not divisible by any of these numbers, the program should display an appropriate message.
number = int(input("Type a number: "))
if not number % 3 == 0 and not number % 5 == 0 and not number % 7 == 0:
    print("The number is not divisible by 3, 5 and 7.")
elif number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
    print("The number is divisible by 3, 5 and 7.")
elif number % 3 == 0:
    print("The number is divisible by 3.")
elif number % 5 == 0:
    print("The number is divisible by 5.")
elif number % 7 == 0:
    print("The number is divisible by 7.")

# 4 - Write a program that will display the following results for the specified variable:
#  ◦ the difference between the value of this variable and 17 if the difference is less than 17
#  ◦ o the square of this difference, otherwise.
number = int(input("You know what to do here, bring that number up: "))
difference = number - 17
if difference < 17:
    print(difference)
else:
    print(difference ** 2)

# 5 - Write a program that returns the sum of the three numbers given.
#  If all three numbers are equal, the program will return the triple value of their sum..
a = int(input("Insert the 1st number: "))
b = int(input("Write the 2nd number: "))
c = int(input("Chose the 3rd number: "))
if a == b == c:
    print((a + b + c) * 3)
else:
    print(a + b + c)

'''WHILE LOOPS EXERCISES'''
# 1 - Write a program that displays all natural numbers between 0 and 50.
x = 0
while x < 50:
    x = x + 1
    print(x)

# 2 - Write a program that displays all even numbers between 0 and 100.
x = 0
while x <= 100:
    if x % 2 == 0:
        print(x)
    x = x + 1

# 3 - Write a program that displays the squares of all integers between 0 and 10.
x = 0
while x <= 10:
    if x <= 10:
        print(x * 2)
    x = x + 1

# 4 - Using the loop, write numbers from -20 to 20.
num = -20
while num <= 20:
    print(num)
    num += 1

#  Then write: the first 6 numbers
num = -20
count = 0
while count < 6:
    print(num)
    num += 1
    count += 1

#  the last 6 numbers
num = 15
count = 0
while count < 6:
    print(num)
    num += 1
    count += 1

#  all even numbers
num = -20
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

#  all numbers except digit 5
num = -20
while num <= 20:
    if "5" not in str(num):
        print(num)
    num += 1

#  all numbers up to and including digit 7
num = -20
while num <= 7:
    print(num)
    num += 1

#  all numbers divisible by 3
num = -20
while num <= 20:
    if num % 3 == 0:
        print(num)
    num += 1

#  the sum of all numbers
num = -20
total_sum = 0
while num <= 20:
    total_sum += num
    num += 1
print(f"The sum of all numbers from -20 to 20 is: {total_sum}")

#  the sum of numbers greater than or equal to 4
num = -20
total_sum = 0
while num <= 20:
    if num >= 4:
        total_sum += num
    num += 1
print(f"The sum of all numbers from -20 to 20, greater than or equal to 4 is: {total_sum}")

#  all numbers and their powers
num = -20
while num <= 20:
    print(f"Number: {num}, Square: {num ** 2}")
    num += 1

#  all numbers and their values for modulo 10
num = -20
while num <= 20:
    print(f"Number: {num}, Modulo 10: {num % 10}")
    num += 1

# 5 - Write a program that displays numbers that are multiples of 5 and are divisible by 7
#  within the range from 1500 to 2700.
num = 1500
while num <= 2700:
    if num % 5 == 0 and num % 7 == 0:
        print(num)
    num += 1

# 6 - Write a program that writes numbers from 0 to 6 and omits 3 and 6.
#  Do it in two versions: with and without the continue statement.
num = 0
while num <= 6:
    if num == 3 or num == 6:
        num += 1
        continue
    print(num)
    num += 1

num = 0
while num <= 6:
    if num != 3 and num != 6:
        print(num)
    num += 1

'''LIST / FOR LOOP EXERCISE'''
# 1 - Write a program that will display, one by one, all items together with their types for a given list.
#  For the following list: a_list = [4, True, None]
#  the program should display the following result:
#  4 <class 'int'>
#  True <class 'bool'>
#  None <class 'NoneType'>
a_list = [4, True, None]
for item in a_list:
    print(item, type(item))

'''SUMMARY OF PART 1 EXERCISES'''
# 1 - A 10-element array is given: a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7].
#  Write a program that prints:
#  ◦ all digits
a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]
for digits in a_list:
    print(digits)

#  ◦ the first 6 digits
a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]
print(*a_list[:6])

#  ◦ the last 6 digits
a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]
print(*a_list[-6:])

#  ◦ all even digits
a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]
for digits in a_list:
    if digits % 2 == 0:
        print(digits)

#  ◦ all digits on odd indexes
a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]
print(a_list[1::2])

#  ◦ all digits except digit 5
a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]
for digits in a_list:
    if digits != 5:
        print(digits)

#  ◦ all digits up to and including digit 7
a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]
index_7 = a_list.index(7)
print(a_list[:index_7 + 1])

#  ◦ all digits divisible by 3
a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]
for digits in a_list:
    if digits % 3 == 0:
        print(digits)

#  ◦ the sum of all digits
a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]
total_sum = sum(a_list)
print(f"Sum of all digits: {total_sum}")

#  ◦ the sum of digits greater than or equal to 4
a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]
total_sum = sum(x for x in a_list if x >= 4)
print(f"Sum of digits >= 4: {total_sum}")

#  ◦ the smallest and the largest digit.
a_list = [1, 3, 5, 2, 5, 6, 7, 4, 9, 7]
print(min(a_list), "and", max(a_list))

# 2 - Write a program that for the given number of words, e.g.
#  a_list = [‘cat’, ‘primer’, ‘window’, ‘computer’] will display subsequent items of the list
#  together with information about the length of these items.
a_list = ["cat", "primer", "window", "computer"]
for word in a_list:
    print(word, len(word))

# 3 - Write a program that for the given list of words, e.g.
#  list_of_words = ["spam", "table", "spam", "brown", "air", "malware", "spam", "end"]
#  will display only the list items that have no “spam” value. In addition, if the list item value is “malware”,
#  the program should terminate operation immediately. Use the break statement.
#  Search in the Internet for information on how the break statement works.
list_of_words = ["spam", "table", "spam", "brown", "air", "malware", "spam", "end"]
for word in list_of_words:
    if word == "spam":
        continue
    elif word == "malware":
        break
    print(word)
