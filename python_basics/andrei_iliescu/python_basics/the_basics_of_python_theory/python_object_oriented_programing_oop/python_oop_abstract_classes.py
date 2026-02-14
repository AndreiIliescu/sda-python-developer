# Clase abstracte (abstract classes) - clase care servesc ca șabloane pentru clase derivate. Ele pot defini metode care trebuie implementate de subclase, fără a oferi corpuri concrete (implementări):contentReference[oaicite:0]{index=0}. Folosim modulul `abc`: definiția se face prin moștenirea din `ABC` (sau cu metaclasa `ABCMeta`), iar metodele abstracte se marchează cu decoratorul `@abstractmethod`:contentReference[oaicite:1]{index=1}. O clasă abstractă nu poate fi instanțiată dacă are metode abstracte nerezolvate; subclasele concrete trebuie să ofere implementări pentru toate metodele abstracte.

# Exemplu 1: clasa abstractă Forma cu metoda abstractă arie()
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def arie(self):
        pass  # metoda abstractă, fără implementare

class Cerc(Forma):
    def __init__(self, raza):
        self.raza = raza
    def arie(self):
        return 3.14159 * self.raza ** 2

c = Cerc(5)  # instanțiem clasa concretă
print(f"Aria cercului de rază {c.raza} este {c.arie()}")  # afișează aria cercului


# Exemplu 2: ierarhie de vehicule cu metode abstracte
class Vehicul(ABC):
    @abstractmethod
    def porneste(self):
        pass
    @abstractmethod
    def opreste(self):
        pass

class Masina(Vehicul):
    def __init__(self, model):
        self.model = model
    def porneste(self):
        print(f"Mașina {self.model} a pornit.")
    def opreste(self):
        print(f"Mașina {self.model} s-a oprit.")

class Bicicleta(Vehicul):
    def __init__(self, tip):
        self.tip = tip
    def porneste(self):
        print(f"Bicicleta {self.tip} începe să meargă.")
    def opreste(self):
        print(f"Bicicleta {self.tip} a încetat mersul.")

m = Masina("Dacia")
m.porneste()
m.opreste()
b = Bicicleta("de munte")
b.porneste()
b.opreste()
