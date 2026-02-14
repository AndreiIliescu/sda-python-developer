### Formatarea textului
# 3 metode comune:
# 1. Operatorul '%' (vechi):
print("Salut, %s. Ai %d ani." % ("Ion", 20))
# 2. metoda str.format():
print("Salut, {}! {} + {} = {}".format("Maria", 2, 3, 2+3))
# 3. f-string (Python 3.6+):
nume = "Elena"
an = 30
print(f"{nume} are {an} ani.")
