### Context Managers ###

# Exemplu de context manager din Python cu "with".
# f = open("test.txt", "w")
# f.write("text scris in fisier")
# f.close()

# Echivalent cu a scrie:

# with open("test.txt", "w") as f:
#   f.write("text scris in fisier")

class MyContextManager:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("Am intrat in context")
        print(f"Name is: {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Am iesit din context")


with MyContextManager("First CM"):
    print("Se executa niste cod")


print("Am ajuns la final")
