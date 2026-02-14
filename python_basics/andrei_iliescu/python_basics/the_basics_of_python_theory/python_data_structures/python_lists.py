### Liste (lists)
# Colecție ordonată și indexată de valori, poate conține elemente de orice tip.
# Exemplu 1:
lista = [1, "doi", 3.0]
print(lista[0], lista[1], lista[-1])


# Exemplu 2: concatenare și buclă:
l1 = [1, 2, 3]
l2 = ["a", "b"]
l3 = l1 + l2  # [1, 2, 3, 'a', 'b']
print(l3)
for element in l3:
    print(f"Element: {element}")


# Exemplu 3: manipularea listelor
lista = [1, 2, 3]
lista.append(4)          # adaugă la finalul listei
lista.insert(1, 1.5)     # inserează valoarea 1.5 la indexul 1
print("Lista inițială după adăugări:", lista)
lista.remove(2)          # elimină prima apariție a valorii 2
print("Lista după remove(2):", lista)
ultimul = lista.pop()    # elimină și returnează ultimul element
print("Element extras cu pop():", ultimul)
print("Lista finală:", lista)
