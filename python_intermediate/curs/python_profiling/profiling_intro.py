### Code profiling ###
import timeit
from math import sqrt

# "timeit.timeit(stmt, setup, number)"
# stmt = codul cronometrat
# setup = imports, partea de inceput a programului
# number = de cate ori va rula codul

# Importuri folosite in interiorul "timeit"
# Trebuie sa importam inclusiv functiile declarate de noi

setup = """
from math import sqrt
from __main__ import my_func
"""

# Exemplu de bloc de code
code = """
def func():
    return [sqrt(x) for x in range(100)]
    

func()
"""

# Exemplu de apelat o functie din codul principal
def my_func():
    return [sqrt(x) for x in range(100)]


func_code_call = "my_func()"

t = timeit.timeit(func_code_call, setup, number=100)
print(t)
