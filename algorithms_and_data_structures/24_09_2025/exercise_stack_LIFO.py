''' Stack - LIFO '''

''' Cerinta: Scriem un cod care simuleaza o stiva de carti 
* Metodele de baza pentru o stiva: add_new_book, get_book, all_books 
* Metode magice in Python: "__add__", "__gt__", "__lt__", "__ge__", "__le__", "__str__", "__repr__", "__len__" '''

from typing import List


class BookStack:
    def __init__(self, stack_name: str = "Default stack", category: str = "Genre"):
        self.stack: List[str] = [] # lista care tine cartile
        self.stack_name = stack_name
        self.category = category


    # adauga o noua carte in stiva (PUSH)
    def add_new_book(self, title: str):
        self.stack.append(title)
        return f"The book '{title}' was added to the bookshelf.\n"


    # scoate ultima carte din stiva (POP)
    def get_book(self):
        if self.stack:
            removed_book = self.stack.pop()
            return f"The book '{removed_book}' was removed from the bookshelf.\n"
        else:
            return "The bookshelf is empty, there is nothing to remove." # in cazul in care stiva este goala


    # returneaza toate cartile din stiva
    def all_books(self) -> List[str]:
        return self.stack.copy()


    # metoda pentru adunarea a 2 stive
    def __add__(self, second_stack: "BookStack") -> "BookStack":
        new_stack = BookStack(stack_name=self.stack_name, category=self.category)
        new_stack.stack = self.stack + second_stack.stack # combinam stivele
        return new_stack


    # compara daca stiva curenta are mai multe carti decat a doua stiva
    def __gt__(self, second_stack: "BookStack") -> bool: # gt = grater than
        return len(self.stack) > len(second_stack.stack)


    # comparam daca stiva curenta are mai putine decat a 2 stiva
    def __lt__(self, second_stack: "BookStack") -> bool: # lt = less than
        return len(self.stack) < len(second_stack.stack)


    # compara daca stiva curenta are mai multe carti sau egal decat a doua stiva
    def __ge__(self, second_stack: "BookStack") -> bool:  # ge = grater or equal
        return len(self.stack) >= len(second_stack.stack)


    # compara daca stiva curenta are mai putine carti sau egal decat a doua stiva
    def __le__(self, second_stack: "BookStack") -> bool:  # le = less or equal
        return len(self.stack) <= len(second_stack.stack)


    # metoda pentru a reprezenta stiva ca string simplu
    def __str__(self) -> str:
        return f"Stack: {self.stack_name} with category of books: {self.category}."


    # metoda detaliata a stivei
    def __repr__(self) -> str: # repr = representation
        books =" ".join(self.stack) # concateneaza toate cartile intr-un sir
        return f"stack_name: {self.stack_name}\n category: {self.category}\n books: {books}"


    # metoda care returneaza lungimea stivei (numarul de carti)
    def __len__(self) -> int:
        return len(self.stack)


# Cream o stiva de carti
book = BookStack("My Stack of Books", "Natural")

# Adaugam carti
print(book.add_new_book("Cheetahs"))
print(book.add_new_book("Elephants"))
print(book.add_new_book("Cats"))

her_books = BookStack("Her Stack of Books", "Natural")
her_books.add_new_book("Horses")

# Verificam stiva
print(book.all_books())

# Scoatem ultima carte
print(book.get_book())

# Verificam stiva iar
print(book.all_books())

# Testam metodele magice
combined = book + her_books
print(combined.all_books())

print(combined > her_books)  # True
print(combined <= her_books) # False

print(str(combined))

print(repr(combined))

print(len(combined))
