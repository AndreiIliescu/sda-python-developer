class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    # Functia "__enter__" va fi apelata automat cand ne folosim de cuvantul "with".
    def __enter__(self):
        # Opening the file
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Closing the file
        self.file.close()


# Variabila declarata dupa "as" (adica "f") is va lua valoarea in functie de
# ce returneaza metoda "__enter__".
with FileManager("test.txt", "w") as f:
    f.write("Mesaj din file manager")

print("Am ajuns la final")
