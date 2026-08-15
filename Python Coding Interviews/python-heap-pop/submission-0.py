import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    my_list= []
    while heap:
        my_list.append(heapq.heappop(heap))
    return my_list


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
