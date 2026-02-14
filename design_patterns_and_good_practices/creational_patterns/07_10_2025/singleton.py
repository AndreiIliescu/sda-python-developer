""" 'self' - se refera la instanta unui obiect
           - folosit in metode normale pt. a accesa atribute/functii ale obiectului
'cls' - se refera la clasa in sine
      - folosit in metode de clasa pt. a accesa atribute/functii ale clasei """

# Varianta 1 - implementare Singleton
class Singleton:
    # Atributul de mai jos este atribut al clasei
    __instance = None                       # Variabila privata care va stoca instanta publica

    @classmethod
    def get_instance(cls):
        if not cls.__instance:              # Daca instanta nu exista inca, o cream
            cls.__instance = Singleton()
        return cls.__instance               # Returnam instanta unica


    def __init__(self):
        if not self.__instance:
            print("Instanta comuna nu a fost creata - nu sunt un Singleton!")
        self.val = 0                        # Atribut simplu


    def function(self):
        print(self.val)


a = Singleton.get_instance()
a.function()
a.val = 10   # Modificam atributul 'val' al instantei unice si il setam la 10
a.function() # Metoda 'function()' afiseaza 'self.val' (a.val = 10) -> output: 10

# In 'Singleton' exista o singura instanta, deci 'b' nu este un obiect nou
# Deci 'b' este exact acelasi obiect ca 'a'
b = Singleton.get_instance()
b.function()
print()

# Concluzie:
# Singleton garanteaza ca toate variabilele de instanta si metodele folosesc aceeasi instanta

# Problema: daca instantiem clasa direct, nu prin 'get_instance()',
# -> instanta nu mai este un singleton
# Solutie: clasa interna + metoda '__new__' pt. separare functionalitati

# Varianta 2 - implementare Singleton
class Singleton:
    class __Singleton:
        def __init__(self):
            self.val = None                                  # Atributul instantei interne


        def __str__(self):
            return repr(self) + str(self.val)                # Reprezentare ca string


    __instance = None                                        # Instanta singleton globala

    def __new__(cls):
        if not Singleton.__instance:
            Singleton.__instance = Singleton.__Singleton()   # Cream instanta doar odata
        return Singleton.__instance                          # Returnam instanta unica


x = Singleton()
x.val = 'test01'
print(x)

y = Singleton()
print(y)
# 'x' si 'y' sunt doua variabile diferite care indica acelasi obiect in memorie
# Cand atributul 'val' se modifica prin 'y', se schimba si pt. 'x'

y.val = 'test02'
print(y)
print(x)
print()

# Varianta 3 - implementare Singleton
# O varianta mai avansata si mai eleganta decat celelalte (folosim decoratorul '@Singleton')
# Scop:
# - poti transforma orice clasa in Singleton fara sa ii modifici codul inter
# - o solutie reutilizabila - doar ii pui decoratorul

def Singleton(class_):
    __instances = {}                                          # Dictionar pentru a stoca instantele unice

    def get_instance(*args, **kwargs):
        if class_ not in __instances:
            __instances[class_] = class_(*args, **kwargs)     # Cream instanta o singura data
        return __instances[class_]                            # Returnam instanta

    return get_instance                                       # returnam functia decoratoare
                                                              # Daca punem 'get_instance()' -> returneaza o instanta
                                                              # (obiect), nu o functie apelabila


# Folosim decoratorul
@Singleton
class FirstClass:
    def __init__(self):
        self.val = 0


@Singleton
class SecondClass:
    def __init__(self):
        self.val = 0


# Testare - instante ale clasei 'FirstClass():'
a = FirstClass()
print(a.val)
a.val = 10
print(a.val)
b = FirstClass()
print(b.val) # Va fi tot 10 deoarece insta este aceeasi

# Testare - instante ale clasei 'SecondClass():'
c = SecondClass()
print(c.val)
c.val = 20
print(c.val)
d = SecondClass()
print(d.val)
print()

# Varianta 4 - implementare Singleton
# Implementare cu metaclasa

class SingletonType(type):
  _instances = {}                                           # Stocam instantele unice

  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
    return cls._instances[cls]                              # Returnam instanta unica


class SingletonClass(metaclass=SingletonType):
  pass


x = SingletonClass()
y = SingletonClass()

print(x == y)
print()

# Varianta 5 - implementare Singleton

class Borg:
    _shared_state = {}                              # Dictionar comun pt. toate instantele

    def __init__(self):
        self.__dict__ = self._shared_state          # Toate instantele impart acelasi spatiu de stocare


class Singleton(Borg):
    def __init__(self, arg):
        Borg.__init__(self)                         # Initializam starea comuna
        self.val = arg                              # Atribuim valoarea argumentului

    def __str__(self):
        return self.val                             # Afisam valoarea


# Testare 'Borg'
x = Singleton('apple')                              # '_shared_state' este gol -> 'x.val' = 'apple'
print(x)
                                                    # Toate instantele viitoare vor avea acelasi dictionar intern
y = Singleton('pear')                               # 'y.__dict__' = 'x.__dict__' (acelasi obiect)
print(y)                                            # 'self.val' = 'pear' -> 'x.val' si 'z.val' se modifica si ele pt.
                                                    # ca folosesc acelasi '__dict__'
z = Singleton('plum')                               # 'z.val' = 'cherry' -> se modifica pentru toate
print(z)
print(x)
print(y)

# 'Borg' nu este Singleton efectiv, dar este o varianta eleganta cand vrei mai multe instante care partajeaza aceeasi
# stare globala.
