from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    hash_map = defaultdict(int)
    for ch in s:
        hash_map[ch] +=1
    return hash_map


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    hash_map = defaultdict(list)
    for sublist in nums:
        first = sublist[0]
        for n in range(1,len(sublist)):
            hash_map[first].append(sublist[n])
    return hash_map


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
