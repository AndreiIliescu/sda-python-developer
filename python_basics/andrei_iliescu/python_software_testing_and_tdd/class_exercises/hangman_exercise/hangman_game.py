def hangman_validator(guess):
    if not isinstance(guess, str):
        return "The data type must be some text"
    if len(guess) < 1:
        return "Guessed text can not be empty"

    if not guess.isalpha():
        return "The text can not contain special characters"

    if guess not in "abc":
        return False
    if len(guess) == 1 and guess in "abc":
        return True

    while True:
        user_guess = input("Guess a letter: ")
        guess_user = hangman_validator(guess)
        if guess_user is not True:
            print("Guess_user")

        return False
