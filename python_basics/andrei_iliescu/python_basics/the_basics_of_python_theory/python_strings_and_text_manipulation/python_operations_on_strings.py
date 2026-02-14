### Operații cu șiruri
# Șirurile sunt secvențe imutabile de caractere.
# Se pot construi cu ghilimele simple, duble sau triple pentru multiline.
s1 = "Ana"
s2 = 'Are'
s3 = """mere"""
print(s1, s2, s3)

# Concatenare și repetare:
print("Salut " + s1 + "!" )
print("Hi!" * 3)

# Acces prin index și slicing:
text = "Python"
print(text[0], text[-1], text[1:4])  # 'P', 'n', 'yth'

# Funcții utile:
print("lungime:", len(text))
print("upper:", text.upper())
