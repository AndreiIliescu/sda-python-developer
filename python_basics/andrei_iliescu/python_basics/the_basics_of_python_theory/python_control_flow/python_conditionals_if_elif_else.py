### if, elif, else
# Instrucțiuni condiționale care permit ramificarea codului:
# if verifică o condiție; elif (else if) oferă noi condiții; else tratează cazul final.
# Exemplu 1:
x = 10
if x > 0:
    print(f"{x} este pozitiv")
elif x == 0:
    print(f"{x} este zero")
else:
    print(f"{x} este negativ")


# Exemplu 2, cu condiții multiple:
nota = 87
if nota >= 90:
    calificativ = "A"
elif nota >= 80:
    calificativ = "B"
elif nota >= 70:
    calificativ = "C"
elif nota >= 60:
    calificativ = "D"
else:
    calificativ = "F"
print(f"Calificativul pentru nota {nota} este {calificativ}.")
