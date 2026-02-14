import copy
import random
import time
from typing import List, Callable


# functie care genereaza liste randon cu numere intregi
def get_random_lists(lengths_of_lists: List[int]) -> List[List[int]]:
    random_lists = []
    for length in lengths_of_lists:
        random_lists.append([random.randint(0, 100) for _ in range(length)])
    return random_lists


input_lengths = [1, 3, 5] # vrem 3 liste, una cu 1 element, una cu 3 si una cu 5
random_lists = get_random_lists(input_lengths)
print("Liste generate random:", random_lists)

# functie care masoara timpul de executie al unei functii de sortare pe fiecare lista
def get_times(lists: List[List[int]], sort_function: Callable[[List[int]], List[int]]) -> List[float]:
    temp_list = copy.deepcopy(lists)
    times = []
    for temp_list in temp_list:
        start_time = time.time()
        sort_function(temp_list)
        end_time = time.time()
        times.append(end_time - start_time)
    return times


timpi_sortare = get_times(random_lists, sorted)
print("Timpi de executie pentru sorted():", timpi_sortare)

# [1.1205673217773438e-05, 4.0531158447265625e-06, 9.5367431640625e-07]
# 1.12 * 10^-5
# 4.05 * 10^-6
# 9.53 * 10^-7
