import datetime
import time


# Folosind pattern-ul Singleton, creaza o clasa "Logger" care scrie siruri de caractere (data si ora) curente
# Folosim o clasa interna (nested) care se contina functionalitatea instantei si suprascrie metoda "__new__" pt.
# implementarea Singleton-ului

class Logger:
    class __Singleton: # Clasa nested care contine functionalitatea efectiva
        def __init__(self, file_name):
            self._file_name =file_name

        def log(self, log_msg):
            with open(self._file_name, "a") as file:
                file.write(f"{datetime.datetime.now()} : {log_msg}\n")

    __instance = None # Variabila statica pt. instanta unica a Singleton-ului

    def __new__(cls, file_name):
        # Daca nu exista inca o instanta, o cream
        if not Logger.__instance:
            Logger.__instance = Logger.__Singleton(file_name)
        # Returnam intotdeauna aceeasi instanta
        return Logger.__instance


# Exemplu de folosire a logger-ului
def main():
    # Cream instanta Logger-ului
    logger = Logger("Logger-file.log") # Fisierele de logger au in general extensia ".log"
    # Scriem 3 mesaje in fisier cu pauze intre ele (pauze cu modulul "time.sleep()")
    logger.log("Primul mesaj din Logger.\n")
    time.sleep(3) # Pauza de 3 secunde
    logger.log("Al doilea mesaj din Logger.\n")
    time.sleep(5) # Pauza de 5 secunde
    logger.log("Al treilea mesaj din Logger.\n")

if __name__ == "__main__":
    main()

# Explicatie:
# "Logger" foloseste pattern-ul "Singleton", astfel incat exista o singura instanta
# "__Singleton" este clasa nested care face efectiv logarea
# "__new__" verifica daca instanta exista, daca nu, o creaza
