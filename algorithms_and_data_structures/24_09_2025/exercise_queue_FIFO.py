''' Queue - FIFO '''

''' Cerinta: Simularea unei cozi de clienti 
- avem 3 tipuri de clienti:
1. femei;
2. barbati;
3. copii.

- fiecare grup trebuie abordat diferit:
* Femei: prefix "Doamna;"
* Barbati: prefic: "Domnul";
* Copii: fara prefix.

- fiecare clasa mostenitoare trebuie sa aiba propria reprezentare ca sir de caractere (__str__)'''
import abc


class Client(abc.ABC):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    # metoda abstracta pentru reprezentarea clientului ca sir de caractere
    @abc.abstractmethod
    def __str__(self) -> str:
        pass


# sa avem pe return un f"string" cu first_name si last_name
class Woman(Client):
    def __str__(self) -> str:
        return f"Doamna {self.first_name} {self.last_name}"


# sa avem pe return un f"string" cu first_name si last_name
class Man(Client):
   def __str__(self) -> str:
        return f"Domnul {self.first_name} {self.last_name}"


# sa avem pe return un f"string" cu first_name si last_name
class Child(Client):
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


# implementarea cozii FIFO
class FifoList:
    def __init__(self):
        self.data = [] # lista care stocheaza clienti


    # adaugam clientul al coda
    def add_client(self, client: Client):
        self.data.append(client)


    # scoatem primul client din coada (FIFO)
    def remove_first_client(self) -> Client:
        if self.data:
            return self.data.pop(0)
        return None


    # afisam toata coada
    def __str__(self):
        return " -> ".join(str(client) for client in self.data)


c1 = Woman("Raluca", "Rotaru")
c2 = Man("Mircea", "Ion")
c3 = Child("Mihai", "Dumitrescu")

print(c1)
print(c2)
print(c3)

queue = FifoList()
queue.add_client(c1)
queue.add_client(c2)
queue.add_client(c3)

print(queue)

queue.remove_first_client() # elimina ce avem la indexul 0 (primul element) -> (primul intrat, primul servit)

print(queue)

''' Casa de marcat (Cash Register)
- trebuie implementare a unei clase care simuleaza operatiile unei magazin
- casa de marcat trebuie sa aiba:
1. O coada FIFO (folosim clasa FifoList pe care am implementat-o)
2. O metoda prin care clientii se pot aseza la coada
3. O metoda prin care clientii sunt procesati in ordinea sosirii (FIFO)

# Pe scurt, clientul intra in coada (se adauga la coada FIFO), casa de marcat proceseaza primul client (cel mai vechi 
din coada) '''

class CashRegister:
    def __init__(self):
        self.queue = FifoList() # Fiecare casa de marcat are o coada FIFO


    # metoda pentru adaugarea unui client la coada
    def add_client_in_queue(self, client: Client):
        self.queue.add_client(client)
        # print(f"{client} join to queue")


    # metoda pentru procesarea unui client (primul intrat)
    def process(self):
        client = self.queue.remove_first_client() # scoatem primul client din coada
        if client:
            return
            print(f"Support {client}")
        else:
            print("No clients in queue")


# cream clientii
client1 = Woman("Anna", "Johnson")
client2 = Man("John", "Smith")
client3 = Child("Chris", "Novak")

# cream casa de marcat
cr = CashRegister()

# adaugam clienti la coada
cr.add_client_in_queue(client1)
cr.add_client_in_queue(client2)
cr.add_client_in_queue(client3)

# procesam clientii (FIFO)
cr.process()
cr.process()
cr.process()

# Verificam coada curenta (ar trebui sa fie goala)
print(cr.queue)

''' Tema pentru data viitoare, exercitiul 2.4 de pe Learnify '''

# Exercise 2.4
''' Facem exact ca la ex. 2.3, doar ca folosim o metoda mai eficienta pt. volume mari de date '''

from collections import deque # special gandit pentru operatii eficiente la ambele capete ale structurii de date


class FasterCashRegister(CashRegister): # Definim o clasa noua ce mosteneste "CashRegister"
    def __init__(self):
        super().__init__()
        self.queue = deque() # Initializam coada ca "deque" (in loc de lista)


    # Metoda pentru adaugare client la sfaritul cozii (FIFO) + mesaj de confirmare
    def add_client_in_queue(self, client: Client):
        self.queue.append(client)
        # print(f"{client} join to queue (faster)")


    # Metoda pentru procesarea clientului
    def process(self):
        if self.queue:
            client = self.queue.popleft() # Scoatem primul client din coada (FIFO, foarte rapid cu "deque")
            # print(f"Support {client}")
        else:
            print("No clients in queue")


# Cream clientii
client1 = Woman("Anna", "Johnson")
client2 = Man("John", "Smith")
client3 = Child("Chris", "Novak")

# Cream casa de marcat rapida (FasterCashRegister)
fcr = FasterCashRegister()

# Adaugam clienti la coada rapida
fcr.add_client_in_queue(client1)
fcr.add_client_in_queue(client2)
fcr.add_client_in_queue(client3)

# Procesam clientii (FIFO) - rapid
fcr.process()
fcr.process()
fcr.process()
fcr.process()

# Verificam coada curenta
print(fcr.queue)
print()

''' ex. 2.5 Comparam durata actiunii in cazul punctelor 2.3 si 2.4 
- salvam timpul curent (T1)
- cream o casa de marcat normala, adaugam 10000 clienti in coada (ex. 2.3)
- procesam clientii
- eliminam clientii
- salvam aici timpul curent din nou (T2)
- afisam cat a durat executia (in secunde), adica t_total = T2 - T1 (timpul de aici - timpul de la inceput)
- apoi aceeasi paisi de mai sus pentru ex. 2.4'''

import time


start_timer = time.time()

cash_register_version = CashRegister()
for client in range(10_001):
    cash_register_version.add_client_in_queue(client1)
for client in range(10_001):
    cash_register_version.process()
print(f"TIme for normal cash register:{time.time() - start_timer}")


cash_register_faster_version = FasterCashRegister()
for client in range(10_001):
    cash_register_faster_version.add_client_in_queue(client2)
for client in range(10_001):
    cash_register_faster_version.process()
print(f"Time for faster cash register: {time.time() - start_timer}")
