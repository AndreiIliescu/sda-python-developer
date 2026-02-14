def cows_and_bulls(generated_number, guess, chances):
    user_input = '1234678787'
    if not isinstance(chances, int):
        return 'Error: the chances parameter must be int'
    if chances < 1:
        return 'Error: the chances must be greater than 0'
    if chances >10:
        return 'Error: the chances must be less than 10'

    if not isinstance(guess,str):
        return 'Error: the guess is not a valid type '

    if len(guess) != 4:
        return 'Error: only 4 characters'

    if not guess.isdigit():
        return 'Error guess must contain only digits'

    if not isinstance(generated_number,str):
        return 'Error: the generated_number is not a valid type '

    if len(generated_number) != 4:
        return 'Error: only 4 characters'

    if not generated_number.isdigit():
        return 'Error generated_number must contain only digits'


    return 'Ana are mere si pere'
