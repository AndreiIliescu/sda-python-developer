### Conversia tipurilor (type conversion)
# Funcții de conversie:
# int(x), float(x), str(x), bool(x), complex(x)
# Exemplu 1 de conversie:
val_str = "100"
val_int = int(val_str)
print(val_int, type(val_int))


# Exemplu 2 de conversie și combinații:
val1 = "3.5"
val2 = 2
suma = float(val1) + val2  # 5.5
text = "Rezultat: " + str(suma)
print(text)
