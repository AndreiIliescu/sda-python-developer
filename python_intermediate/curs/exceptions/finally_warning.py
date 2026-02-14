# Atentie!
# Codul din finally se va executa mereu, indiferent de ce este scris in try/except

def my_func():
    try:
        return "a"
    except Exception:
        return "b"
    finally:
        print("c")


print(my_func())
