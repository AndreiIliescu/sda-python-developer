### for loop
# Iterează prin elementele unei colecții (liste, șiruri de caractere, etc.):
# Exemplu 1 de buclă for:
animale = ["câine", "pisică", "pește"]
for animal in animale:
    print(f"Animal: {animal}")


# Exemplu 2: iterare cu enumerate pentru index și valoare:
fructe = ["măr", "banană", "portocală"]
for index, fruct in enumerate(fructe, start=1):
    print(f"{index}: {fruct}")
