''' Aici discutam de lista ca structura de date (diferit fata de tipul de date "list" care este built-in in Python)

Lista unidirectionala (singly linked list)
Head -> [data|next] -> [data|next] -> [data|next] -> None

Lista bidirectionala (doubly linked list)
Head -> [prev|data|next] <-> [prev|data|next] <-> [prev|data|next] <- Tail
- prev = pointer catre elementul anterior
- next = pointer catre elementul urmator


Lista (ca structura de date) = o colectie de noduri conectate prin printeri
- este eficienta pentru insertii/stergeri '''

# Lista unidirectionala

# definim nodul (contine data + pointer "next")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# definim lista unidirectionala
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0                           # numarul de elemente din lista


    # adaugam un element la finalul listei
    def append(self, data):
        new_node = Node(data)                      # cream un nou nod
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node              # legam ultimul nod la nodul nou
            self.tail = new_node                   # actualizam tail
        self.counter += 1


    # afisam toate elementele listei
    def __str__(self):
        # putem crea o lista goala "elements" in care salvam valorile nodurilor pe masura ce parcurgem lista
        elements = []
        current = self.head
        while current: # bucla atata timp cat exista un nod ("current" nu e None)
            elements.append(str(current.data))
            current = current.next # trecem la urmatorul nod din lista folosind pointer-ul "next"
        return " -> ".join(elements)


    # cautam un element dupa valoare
    def find(self, value):
        current = self.head # pornim de la primul nod al listei (head)
        index = 0 # folosim un pointer temporar ("current") folosit pt. a parcurge lista
        while current: # bucla pentru cat timp exista un nod (adica "current" nu este None)
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1


    # metoda pentru a sterge un nod dupa valoare
    def remove(self, value):
        current = self.head
        previous = None
        while current:
            if current.data == value:
                if previous:
                    previous.next = current.next # legam nodul anterior la urmatorul nod
                else:
                    self.head = current.next # actualizam head sa fie urmatorul ndd

                if current == self.tail:
                    self.tail = previous # actualizam tail sa fie nodul anterior
                self.counter -= 1 # scadem contorul de noduri
                return True # stergerea a reusit
            previous = current # actualizam previous sa fie nodul curent
            current = current.next # trecem la urmatorul nod din lista
        return False


ll = LinkedList() # heads si tail sunt None

ll.append(10) # adaugam un nod cu valoarea 10 (devine si head si tail)
ll.append(20) # adaugam un nod cu valoarea 20 (Legam 10 -> 20, iar tail devine 20)
ll.append(30) # adaugam un nod cu valoarea 20 (Legam 20 -> 30, iar tail devine 30)

print("LinkedList")
print(ll)

node = ll.find(20) # cauta nodul care contine valoare 20 (parcurgem de la head pana il gasim)
print(node)

ll.remove(20) # stergem primul nod cu valoarea 20, apoi refacem legaturile: 10 -> 30


# Lista bidirectionala

# definim nodul (contine data + pointer "next" + pointer "prev")
class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None # primul element al listei
        self.tail = None
        self.count = 0

    # adaugam un element la finalul listei
    def append(self, data):
        new_node = Node2(data)  # cream un nou nod
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail # legam nodul la tail
            self.tail.next = new_node  # tail-ul anterior face point la noul nod
            self.tail = new_node  # actualizam tail
        self.count += 1

    # afisam lista de la head la tail
    def __str__(self):
        # putem crea o lista goala "elements" in care salvam valorile nodurilor pe masura ce parcurgem lista
        elements = []
        current = self.head
        while current:  # bucla atata timp cat exista un nod ("current" nu e None)
            elements.append(str(current.data))
            current = current.next  # trecem la urmatorul nod din lista folosind pointer-ul "next"
        return " -> ".join(elements)


    # afisam lista de la tail la head (traversarea inversa)
    def reverse_string(self):
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        return " <- ".join(elements) # "join" il folosim cand vrem sa lipim mai multe string-uri intr-un singur string


    def find(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None


    # stergem primul element cu o anumita valoare
    def remove(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev: # daca nodul nu este primul
                    current.prev.next = current.next # legam nodul anterior la urmatorul
                else:
                    self.head = current.next # actualizam "head" la urmatorul nod

                if current.next: # daca nodul nu este ultimul
                    current.next.prev = current.prev # legam nodul urmator la nodul anterior
                else:
                    self.tail = current.prev # actializam "tail" la nodul anterior

                self.count -= 1
                return True # confirmam ca am sters elementul

            current = current.next # trecem la urmatorul nod

        return False # daca am parcurs toata lista si nu am gasit valoarea


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

print("DoublyLinkedList:")
print(dll)

print(dll.reverse_string()) # ne arata lista inversa

node = dll.find(20)
print(node.data)

dll.remove(20)

print(dll)

print(dll.reverse_string())
