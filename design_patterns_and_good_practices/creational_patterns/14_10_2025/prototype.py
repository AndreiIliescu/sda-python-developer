import copy


""" Este un tipar de design, ce permite crearea de obiecte printr-un proces impartit in doua etape:
1. Crearea unui obiect de baza - care este o copie a obiectului final;
2. Setarea celorlalte campuri ale obiectului.

Copierea in Python:
- Shallow Copy (copiere superficiala) """
# ex. Shallow Copy:
original = [1, [2, 3]]
shallow = copy.copy(original)

shallow[0] = 10 # Schimbarea valorii simple nu afecteaza originalul
shallow[1][0] = 20 # Schimbarea listei interne afecteaza si originalul

print(original) # [1, [20, 3]]

""" - Deep Copy (copiere profunda) """
# ex. Deep Copy:
original = [1, [2, 3]]
deep = copy.deepcopy(original)

# Modificarile facute in copia "deep" nu afecteaza originalul
deep[0] = 10
deep[1][0] = 20

print(original)
print()

""" Implementare simpla a pattern-ului Prototype folosind modulul 'copy' si o copiere shallow (superficiala) """
# Clasa care reprezinta un fisier Python
class PythonCodeFile:
    def __init__(self, license_content, file_extension, code='', file_name=''):
        self._license_content = license_content       # Continutul licentei
        self._code = code                             # Codul fisierului
        self._file_name = file_name                   # Numele fisierului
        self._file_extension = file_extension         # Extensia fisierului


    @property
    def license_content(self):
        return self._license_content                  # Returneaza continutul licentei


    @license_content.setter
    def license_content(self, value):
        self._license_content = value                 # Seteaza continutul licentei


    @property
    def code(self):
        return self._code                             # Returneaza codul sursa


    @code.setter
    def code(self, value):
        self._code = value                            # Seteaza codul sursa


    @property
    def file_name(self):
        return self._file_name                        # Returneaza numele fisierului


    @file_name.setter
    def file_name(self, value):
        self._file_name = value                       # Seteaza numele fisierului


    @property
    def file_extension(self):
        return self._file_extension                   # Returneaza extensia fisierului


    @file_extension.setter
    def file_extension(self, value):
        self._file_extension = value                  # Seteaza extensia fisierului


    # Metoda pt. crearea unei clone a obiectului (Prototype)
    def create_clone(self):
        return copy.copy(self)                        # Folosim "Shallow Copy"


    # Reprezentare text a obiectului pt. afisare
    def __str__(self):
        return f"File: {self._file_name}.{self._file_extension}, license=[{self._license_content}], code=[{self._code}]"


# Managerul pt. fisiere Python, care foloseste "Prototype" pt. a crea fisiere rapid
class PythonCodeFilesManager:
    _base_file = PythonCodeFile('SDA', 'py')           # Obiect de baza ce va fi clonat


    @staticmethod
    def create_file_with_content(file_name, code):
        base_file_clone = PythonCodeFilesManager._base_file.create_clone()      # Cream o clona
        base_file_clone.file_name = file_name
        base_file_clone.code = code
        return base_file_clone


def main():
    file_1 = PythonCodeFilesManager.create_file_with_content('zen_of_python', 'import this')
    file_2 = PythonCodeFilesManager.create_file_with_content('test_file', 'test')

    print(file_1)
    print(file_2)


if __name__ == '__main__':
    main()
