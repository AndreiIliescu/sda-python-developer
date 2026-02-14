def max_of_three(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        return 'Te rog introdu doar cifre de la tastatura'
    if a < 0 or b < 0 or c < 0:
        return 'Numbers is not positives'
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
