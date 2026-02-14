""" COMPOSITE

Permite tratarea obiectelor individuale si a grupurilor de obiecte intr-un mod uniform.
Creaza o structura ierarhica (ca un arbore), unde frunzele si nodurile compuse sunt tratate la fel de client.
Clientul nu trebuie sa stie daca lucreaza cu un obiect simplu sau un grup de obiecte.
Folosinta: Structura ierarhica (organizatii/fisiere din unele in altele) si vrem sa tratam obiectele individuale si
grupuri in acelasi mod. """

# ex.
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x}, {self._y})"


class Line:
    def draw(self, length):
        pass

    def starting_position(self):
        pass

    def starting_position(self, value):
        pass


class SolidLine(Line):
    def __init__(self):
        self._point = Point(0, 0)

    def draw(self, length):
        print(f"Drawing solid line starting in {self._point} with lenght {length}")

    @property
    def starting_position(self):
        return self._point

    @starting_position.setter
    def starting_position(self, value):
        self._point = value


class DottedLine(Line):
    def __init__(self):
        self._point = Point(0, 0)

    def draw(self, length):
        print(f"Drawing d.o.t.t.e.d line starting in {self._point} with lenght {length}")

    @property
    def starting_position(self):
        return self._point

    @starting_position.setter
    def starting_position(self, value):
        self._point = value


class CompoundLine(Line):
    def __init__(self):
        self._lines = []

    def draw(self, length):
        for line in self._lines:
            line.draw(length)

    @property
    def starting_position(self):
        if not self._lines:
            return Point(0, 0)
        else:
            return self._lines[0].starting_position()

    @starting_position.setter
    def starting_position(self, value):
        for line in self._lines:
            line.starting_position = value

    def add_line(self, line):
        self._lines.append(line)

    def remove_line(self, line):
        self._lines.remove(line)


def main():
    dotted_1 = DottedLine()
    dotted_1.starting_position = (1, 1)

    dotted_2 = DottedLine()
    dotted_2.starting_position = (2, 2)

    solid_1 = SolidLine()
    solid_1.starting_position = (3, 3)

    solid_2 = SolidLine()
    solid_2.starting_position = (4, 4)

    compound_1 = CompoundLine()
    compound_2 = CompoundLine()

    # folding a tree structure
    compound_1.add_line(dotted_1)
    compound_1.add_line(solid_1)
    compound_1.add_line(compound_2)
    compound_2.add_line(dotted_2)
    compound_2.add_line(solid_2)

    # a common interface for a node and a leaf
    compound_2.starting_position = (5, 5)

    solid_2.starting_position = (6, 6)

    compound_1.draw(5)


if __name__ == '__main__':
    main()
