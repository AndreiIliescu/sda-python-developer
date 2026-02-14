import functools


""" Decorator (ca design pattern structural), nu ca functia de 'wrap' din Python.
rol = adauga functionalitate suplimentara unui obiect existent, fara a modifica comportamentul sau de baza """

# Interfata comuna pe care decoratorii o vor implementa
class FragStatistics:
    def increment_frag_count(self):
        pass


    def increment_death_count(self):
        pass


    def reset(self):
        pass # Resetarea statisticilor


# Clasa de baza care stocheaza frag-uri si decese
class FirstPersonShooterFragStatistics(FragStatistics):
    def __init__(self):
        self._frags_count = 0
        self._death_count = 0


    def increment_frag_count(self):
        self._frags_count += 1
        return self._frags_count


    # Incrementam mai jos pt. frag/death si crestem contorul
    def increment_death_count(self):
        self._death_count += 1
        return self._death_count


    # Resetare frag/death
    def reset(self):
        self._frags_count = 0
        self._death_count = 0


# Decorator care adauga mesaj la fiecare deces
class DeathCountInfoDecorator(FragStatistics):
    def __init__(self, frag_statistics):
        self._frag_statistics = frag_statistics                          # Pastreaza obiectul decorat


    def increment_frag_count(self):
        return self._frag_statistics.increment_frag_count()              # Afiseaza functionalitatea originala


    def increment_death_count(self):
        print("Fragged by an enemy")
        return self._frag_statistics.increment_death_count()


    def reset(self):
        self._frag_statistics.reset()                                    # Reseteaza folosind obiectul original


# Decorator care afiseaza statisticile dupa fiecare increment
class DisplayCountersDecorator(FragStatistics):
    def __init__(self, frag_statistics):
        self._frag_statistics = frag_statistics


    def increment_frag_count(self):
        frag_count = self._frag_statistics.increment_frag_count()
        print(f"Your frag count is: {frag_count}")                      # Afiseaza frag-urile curente
        return frag_count


    def increment_death_count(self):
        death_count = self._frag_statistics.increment_death_count()
        print(f"Your death count is: {death_count}")
        return death_count


    def reset(self):
        self._frag_statistics.reset()
        print("Stats reset - KDR is equal to 0")


# Decorator care calculeaza si afiseaza raportul frag/death (KDR)
class FragDeathRatioDecorator(FragStatistics):
    def __init__(self, frag_statistics):
        self._frag_statistics = frag_statistics
        self._current_frag_count = None
        self._current_death_count = None


    def increment_frag_count(self):
        self._current_frag_count = self._frag_statistics.increment_frag_count()
        self._display_frag_deaths_ratio()
        return self._current_frag_count


    def increment_death_count(self):
        self._current_death_count = self._frag_statistics.increment_death_count()
        self._display_frag_deaths_ratio()
        return self._current_death_count


    def _display_frag_deaths_ratio(self):
        if self._current_frag_count and self._current_death_count:
            print(f"KDR is {self._current_frag_count / self._current_death_count}")


    def reset(self):
        self._frag_statistics.reset()


# Decorator care afiseaza mesaj la fiecare frag
class FragInfoDecorator(FragStatistics):
    def __init__(self, frag_statistics):
        self._frag_statistics = frag_statistics


    def increment_frag_count(self):
        print("Enemy fragged")
        return self._frag_statistics.increment_frag_count()


    def increment_death_count(self):
        return self._frag_statistics.increment_death_count()


    def reset(self):
        self._frag_statistics.reset()


# Functia principala care demonstreaza utilizarea decoratorilor
def main():
    statistics = FirstPersonShooterFragStatistics() # Obiectul acesta va tine evidenta frag/decese, dar nu va afisa nimic

    statistics.increment_death_count()  # Incrementam nr. de decese cu 1, la obiectul nedecorat, nu se afiseaza numic pe ecran
    statistics.increment_frag_count()  # Incrementam nr. de frag cu 1, la obiectul nedecorat, nu se afiseaza numic pe ecran

    # Combinam mai multi decoratori
    decorated_statistics = FragDeathRatioDecorator(
        FragInfoDecorator(DisplayCountersDecorator(DeathCountInfoDecorator(statistics))))

    # Aici cream un lant de decoratori
    # 1. DeathCountInfiDecorator(statistics) -> afiseaza mesaj cand jucatorul moare
    # 2. DisplayCountersDecorator(...) -> afiseaza nr. curent de frag/death
    # 3. DisplayCountersDecorator(...) -> afiseaza mesaj la frag
    # 4. FragDeathRatioDecorator(...) -> calculeaza si afiseaza raportul frag/death (KDR)
    # Fiecare metoda apelata va trece prin toti decoratorii, adaugand functionalitati

    # Testam functionalitatea decorata
    decorated_statistics.increment_frag_count()
    decorated_statistics.increment_frag_count()
    decorated_statistics.increment_frag_count()
    decorated_statistics.increment_death_count()


if __name__ == "__main__":
    main()

print()

# Implementare built-in in Python Decorator
# Decoratorul foloseste "functools.wrap" pt. a pastra metoda functiei originale

def cache(fn):
    _cache = dict() # Pastreaza numele si docstring-ul functiei originale

    @functools.wraps(fn)
    def chacher(*args):
        if args not in _cache:
            _cache[args] = fn(*args) # Apeleaza functia si stocheaza rezultatul
        return _cache[args]

    return chacher # Returneaza functia decorata


# Aplicare decorator "chache" asupra functiei Fibinacci
@cache
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n + 1) + fibonacci(n - 2) # Recursivitate pentru Fibonacci


def main():
    print(fibonacci(35)) # Apeleaza functia "fibonacci(35)", folosind cache-ul decoratorului
    # Este al 35-lea nr. din sirul Fibonacci, deci suma dintre al 33-lea si al 34-lea

if __name__ == "__main__":
    main()
