import json


with open("students.json", "w") as f:
    # Exemplul 1
    # students = [
    #     {
    #         "name": "Ana",
    #         "id": 1
    #     },
    #     {
    #         "name": "Alex",
    #         "id": 2
    #     }
    # ]

    # Exemplul 2
    # Definim un dictionar clasic de Python
    students = {
        "studenti": [
            {
                "name": "Ana",
                "id": 1
            },
            {
                "name": "Alex",
                "id": 2
            }
        ],
        "materii": ["Mate", "Romana"],
        "ora": "18:00"
    }

    # Modificam o valoare din dictionar
    students["studenti"][0]["name"] = "Calin"
    students["studenti"].append({"name": "Matei", "id": 5})

    # Scriem tot dictionarul in fisierul json
    json.dump(students, f, indent=4)


with open("students.json", "r") as f:
    my_students = json.load(f)
    print(my_students)
