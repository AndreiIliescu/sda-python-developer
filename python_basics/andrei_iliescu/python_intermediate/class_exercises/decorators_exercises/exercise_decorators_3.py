# Implementati decoratorul no_bad_words(to_exclude) care nu va rula functia daca parametrul ei nu contine cuvantul to_exclude
# Exemplu functie

def no_bad_words(to_exclude):

    def dec(func):

        def wrapper(*args):
            # Prima varianta de cod - nefunctionala
            """if "sad" in to_exclude (nu funcitioneaza)"""
            # A doua varianta de cod - generalizata pe string-ul "sad"
            """if "sad" in args[0]: (functioneaza doar atunci cand cuvantul exclus este strict "sad")"""
            # A treia varianta - functionala indiferent de ce cuvant trebuie exclus
            if to_exclude in args[0]:
                return
            func(*args)

        return wrapper

    return dec


@no_bad_words('sad')
def greet_world(msg):
    print(f"{msg}")


greet_world("Hello happy world!")
greet_world("It's raining, sad world...")
greet_world("It's sunny, hello wonderful world")

# Output
# Hello happy world!
# It's sunny, hello wonderful world
