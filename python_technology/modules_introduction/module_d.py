# importam din modulul_a doar functiile, variabilele care ne intereseaza
from module_a import test, find_index

# ne folosim de variabile si functii dupa numele importate

print(test)

courses = ["Gym", "History", "Math"]
index = find_index(courses, "Math")
print(index)
