# 1 - Sa se defineasca o functie care calculeaza media aritmetica a oricator valori
def arithmetic_mean(*numbers):
    return sum(numbers) / len(numbers)


average = arithmetic_mean(1, 2, 3)
print(average)


# 2 - Sa se defineasca o functie care calculeaza media geometrica a oricator valori
def geometric_mean(*numbers):
    multiplication = 1
    for num in numbers:
        multiplication *= num
    return multiplication ** (1 / len(numbers))


average = geometric_mean(4, 9)
print(average)


# 3 - sa se defineasca o functie pentru rezolvarea ecuatiei de grad 1
# ax + b = 0
def first_degree_equation(a, b):
    return -b / a


solution = first_degree_equation(10, 74)
print(solution)


# 4 - sa se defineasca o functie pentru rezolvarea ecuatiei de grad 2
# ax^2 + bx + c = 0
def second_degree_equation(a, b, c):
        d = b ** 2 - 4 * a * c
        x1 = (-b + d ** (1 / 2)) / (2 * a)
        x2 = (-b - d ** ( 1 / 2)) / (2 * a)
        return x1, x2


solution = second_degree_equation(1, -3, 2)
print(solution)


# 5 - Sa se defineasca o functie care sa primeasca un intreg ca parametru reprezentand baza urmatorului desen:
# - #
# - ##
# - ###
# - ####
# - #####
def hashtag_draw(n):
    for i in range(n):
        print("#" * i)


hashtag_draw(6)
