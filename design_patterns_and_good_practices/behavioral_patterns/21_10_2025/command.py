""" COMMAND

Infasoara un proces intr-un obiect.
Rol: Separa obiectul care emite o comanda de cel care executa comanda.
Transforma un proces intr-un obiect separat.
Scop: Decupleaza logica pe care o are o actiune, de logica pt. executia ei."""

class Command:
    def apply(self):
        pass

    def cancel(self):
        pass


class PythonFile:
    def __init__(self, file_name, lines_content):
        self.file_name = file_name
        self.lines_content = lines_content

    def add_line(self, line):
        self.lines_content.append(line)

    def __str__(self):
        return f"file_name={self.file_name} {self.lines_content}"


class ChangeFileNameCommand(Command):
    def __init__(self, python_file, new_name):
        self._python_file = python_file
        self._new_name = new_name
        self._previous_name = None

    def apply(self):
        self._previous_name = self._python_file.file_name
        self._python_file.file_name = self._new_name
        print(f"File name changed to: {self._new_name}")

    def cancel(self):
        if self._previous_name:
            self._python_file.file_name = self._previous_name
            self._previous_name = None


class RemoveEmptyLinesCommand(Command):
    def __init__(self, python_file):
        self._python_file = python_file

    def apply(self):
        self._python_file.lines_content = [line for line in self._python_file.lines_content if line.strip()]

    def cancel(self):
        print('Operation not supported!')


def main():
    python_file = PythonFile('test.py', ["import this", "    ", "print('That's all folks!)", ""])

    change_file_name_command = ChangeFileNameCommand(python_file, 'zen.py')
    remove_empty_lines_command = RemoveEmptyLinesCommand(python_file)

    change_file_name_command.apply()
    remove_empty_lines_command.apply()

    print(python_file)

    change_file_name_command.cancel()
    remove_empty_lines_command.cancel()

    print(python_file)


if __name__ == '__main__':
    main()
