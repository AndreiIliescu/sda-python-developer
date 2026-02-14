# sys este un modul venit la pachet cu python
import sys

import random

print(sys.path)

# __file__ este o variabila 'magica' (magic method) care contine locatia fisierului in care suntem
print(__file__)

# locatia modului random
print(random.__file__)
