# Implementati decoratorul @repeat_func(num_times) care va repeta functia decorata de 'num_times' ori

def repeat_func(num_times):

    def dec(func):

        def wrapper(*args):
            for repeat in range(num_times):
                func(*args)

        return wrapper

    return dec


# Exemple functie
@repeat_func(num_times=5)
def greet(name):
    print(f'Hello {name}')

greet('Python')


# Output:
# Hello Python
# Hello Python
# Hello Python
# Hello Python
# Hello Python
