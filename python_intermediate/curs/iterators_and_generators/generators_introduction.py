### Generatori ###

# Exemplul 1:
def my_generator():
    a = 1
    print("Am intrat in generator", a)

    # "yield" va "ingheta" functia in stadiul in care este
    # Functia "my_generator()" se continua cand apelam pe ea "next()"
    yield

    print("Din nou in generator", a)

    yield

    print("A treia oara", a)


gen = my_generator()
next(gen)
print("In codul principal")
next(gen)
# next(gen)

print("\n\n")

# Exemplul 2
def even_generator(n):
    current_number = 2
    generated_count = 0

    while generated_count < n:
        yield current_number

        current_number += 2
        generated_count += 1


# even_numbers = even_generator(10)
# print(next(even_numbers))
# print(next(even_numbers))
# print(next(even_numbers))

# sau cu "for"

even_numbers = even_generator(10)
for n in even_numbers:
    print(n)
