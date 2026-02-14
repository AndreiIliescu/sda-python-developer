import heapq # importam modulul "heapq" (implementare min-heap in Python)

# avem o lista nesortata de elemente
numbers = [15, 3, 9, 1, 20, 7]

heapq.heapify(numbers) # reorganizeaza lista ca heap
print("Heap-ul initial", numbers)

sorted_list = []
while numbers:
    smallest = heapq.heappop(numbers) # "heappop" scoate cel mai mic element din heap
    sorted_list.append(smallest)      # il adaugam in lista sortata

print("Lista sortata folosind heap: ", sorted_list)

# Reprezentarea grafica a heap-ului:
#      1
#    /   \
#   3     7
#  / \   / \
# 15 20 9


# Reprezentarea grafica a heap-ului:
# [1, 3, 7, 9, 15, 20]
#      1
#    /   \
#   3     7
#  / \   / \
# 9 15 20
# Se respecta:
# 1 < 3 si 1 < 7
# 3 < 9 si 3 < 15
# 7 < 20
