import csv


with open("employee.csv", "r") as f:
    # Cream in obiect de tip reader care contine datele din fisier
    reader = csv.reader(f)

    # for row in reader:
    #     print(row)

    data = list(reader)

    # Primul element din lista sunt denumirile coloanelor
    print(data[0])

    # Restul elementelor sunt valorile de pe fiecare rand
    print(data[1])


with open("employee.csv", "a", newline="") as f:
    # Cream un obiect "writer" de care ne folosim pentru a scrie date in csv
    writer = csv.writer(f)

    writer.writerow(["Beatrice", 6780])
