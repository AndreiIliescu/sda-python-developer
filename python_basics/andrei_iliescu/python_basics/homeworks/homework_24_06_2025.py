# 1 - Sa se genereze un brad de forma:
#    #
#   ###
#  #####
# #######
size = int(input("Insert size: "))

for i in range(size):
    print(" " * (size - i), "#" * (i * 2 + 1))


# 2 - Sa se genereze un brad cu cer de forma:
# ^^ # ^^
# ^ ### ^
#  #####
# #######
# Hint: base = 57 for i in range(1, base + 1, 2): print()
base = 7

decoration = ["^^", "^"]
line_index = 0

for i in range(1, base + 1, 2):
    spaces = (base - i) // 2
    line = " " * spaces + "#" * i + " " * spaces

    if line_index < len(decoration):
        decor = decoration[line_index]
        line = decor + " " + line.strip() + " " + decor
    else:
        line = line

    print(line)
    line_index += 1


# 3 - Sa se defineasca clasa Student, cu proprietatile first_name, last_name, group.
# Sa se implementeze magic method-urile str, repr
class Student:
    def __init__(self, first_name, last_name, group):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group

    def __str__(self):
        return f"<{self.first_name} {self.last_name} {self.group}>"

    def __repr__(self):
        return f"<{self.first_name} {self.last_name} {self.group}>"


print(Student("Andrei", "Iliescu", "PythonRemote76"))
print([Student("Andrei", "Iliescu", "PythonRemote76"),
       Student("Andrei", "Iliescu", "PythonRemote76")])
