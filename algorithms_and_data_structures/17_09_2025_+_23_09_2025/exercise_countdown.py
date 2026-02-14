### Count Down ###


# O functie recursiva care numara descrescator
# ex.: countdown(5) -> 5, 4, 3, 2, 1 apoi se opreste

def countdown_rec(n):
    if n < 1:
        return
    print(n)
    countdown_rec(n - 1)


countdown_rec(5)

print()

def countdown_iter(n):
    while n > 0:
        print(n)
        n -= 1


countdown_iter(5)
