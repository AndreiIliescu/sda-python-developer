import matplotlib.pyplot as plt # pentru vizualizarea rezultatelor in grafice
import heapq
from typing import List
from functii_auxiliare import get_random_lists, get_times


# Sortari simple pentru ex. cu matplotlib:
def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def quick_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left = [x for x in lst[1:] if x <= pivot]
    right = [x for x in lst[1:] if x > pivot]
    sorted_list = quick_sort(left) + [pivot] + quick_sort(right)
    for i in range(len(lst)):
        lst[i] = sorted_list[i]  # actualizăm lista in-place
    return lst


def heap_sort(lst: List[int]) -> List[int]:
    heapq.heapify(lst)
    sorted_list = [heapq.heappop(lst) for _ in range(len(lst))]
    lst.clear()
    lst.extend(sorted_list)
    return lst


def main():
    lengths = [10, 100, 200, 300, 400, 500, 700, 800, 900, 1000]
    lsts = get_random_lists(lengths)
    quick_sort_results = get_times(lsts, quick_sort)
    bubble_sort_results = get_times(lsts, bubble_sort)
    heap_sort_results = get_times(lsts, heap_sort)
    plt.plot(lengths, quick_sort_results, label='quick')
    plt.plot(lengths, bubble_sort_results, label='bubble')
    plt.plot(lengths, heap_sort_results, label='heap')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
