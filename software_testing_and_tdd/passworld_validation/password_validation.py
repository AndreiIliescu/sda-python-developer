import string


def validate_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    symbols =string.punctuation

    if not isinstance(password, str):
        return "Password is not string!"

    if len(password) < 8:
        return "Minimum 8 characters"

    if len(password) > 16:
        return "Maximum 16 characters"

    for item in password:
        if item.isupper():
            has_upper = True
        elif item.islower():
            has_lower = True
        elif item.isdigit():
            has_digit = True
        elif item in symbols:
            has_symbol = True
    if not has_upper or not has_lower or not has_digit or not has_symbol:
        return False
    return True
