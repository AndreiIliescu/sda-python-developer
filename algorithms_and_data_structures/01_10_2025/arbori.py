''' Implementare arbore

- un arbore este o structura de date din noduri '''

# definim clasa "Node" care va reprezenta fiecare nod din arbore
class Node:
    def __init__(self, data):
        self.data = data                                # valoarea stocata in nod
        self.children = []                              # lista de "child" (fiecare copil este un nod)


    # metoda pentru a adauga un copil la nodul curent
    def add_child(self, child):
        self.children.append(child)


    # metoda pentru afisarea arborelui intr-o maniera ierarhica
    def display(self, level = 0):                       # level indica nivelul nodului in arbore (root = 0)
        print(" " * level * 2 + str(self.data))         # afisam valoarea nodului cu indentare, se multimplica spatiile
                                                        # cu nivelul pt. vizualizare ierarhica
        for child in self.children:
            child.display(level + 1)                    # apelam recursiv "display()" pt. child


if __name__ == "__main__":
    root = Node("A")

    # cream 2 copii ai radacinii: B si C
    B = Node("B")
    C = Node ("C")

    # adaugam pe B si C ca fii ai nodului A
    root.add_child(B)
    root.add_child(C)

    # cream copii pentru bodul B: D si E
    D = Node("D")
    E = Node("E")

    # adaugam pe D si E ca fii a lui B
    B.add_child(D)
    B.add_child(E)

    # cream un copil pentru nodul C: F
    F = Node("F")

    # adaugam pe F ca fiu al lui C
    C.add_child(F)

    # afisam structura arborelui
    print("Structura arborelui: ")
    root.display()

# ======================================================================================================================

''' Arbore binar (binary tree)

- arbore binar = un arbore in care nodurile pot avea maxim 2 copii (child)
- nodurile "child" se numesc "child left" si "child right"

TEMA: 
class Node:
    valoarea stocata in nod
    referinta catre "child left" si "child right"


- definirea clasei BinarySearchTree
class BinarySearchTree:
    radacina arborelui (initial goala) - de implementat in costructor
    
    metoda pentru inserarea unui nou nod in arbore
    def insert(self, data):
        pass
    
    metoda pentru a afisa arborele in ordine
    def in_order(self, Node):
        pass '''

''' Arbore binar cu afișare ierarhică '''

class Node:
    def __init__(self, data):
        self.data = data                       # valoarea stocata in nod
        self.left = None                       # referinta catre copilul din stanga
        self.right = None                      # referinta catre copilul din dreapta


class BinarySearchTree:
    def __init__(self):
        self.root = None                   # radacina arborelui (initial goala)

    # metoda pentru inserarea unui nou nod in arbore
    def insert(self, data):
        if self.root is None:              # arborele este gol
            self.root = Node(data)         # nodul devine radacina
        else:
            self._insert(data, self.root)


    # Metoda recursiva, interna (de obicei "_" sugereaza ca este pt. uz intern)
    def _insert(self, data, current_node):
        if data < current_node.data:       # daca valoarea e mai mica -> mergem in stanga
            if  current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:      # daca valoarea e mai mare -> mergem in dreapta
            if current_node.right is None:
                current_node.right = Node(data) # cream un nod nou
            else:
                self._insert(data, current_node.right)


    # metoda pentru a afisa arborele in ordine (stanga -> radacina -> dreapta
    def in_order(self):
        print("Parcurgere in ordine (in_order)")
        self._in_order(self.root)           # apelam metoda recursiva pe radacina


    def _in_order(self, node):
        if node is not None:                # daca nodul nu e gol
            self._in_order(node.left)       # parcurgem recursiv subarborele stang
            print(node.data, end=" ")
            self._in_order(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree() # cream un arbore binar

    # inseram cateva valori
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    # afisam valorile in ordine
    bst.in_order()
