"""
Synmetric
Input [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
Output [(5, 3), (7, 4)]
"""
from typing import List, Iterator, Tuple


def synmetric_check(array: List[tuple]) -> List[tuple]:
    # myself
    cache = set()
    list = []
    for s in array:
        cache.add((s[1], s[0]))
        if s in cache:
            list.append(s)
    return list


def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
    # coded by Sakai
    cache = {}
    for pair in pairs:
        first, second = pair[0], pair[1]
        value = cache.get(second)
        if not value:
            cache[first] = second
        elif value == first:
            yield pair


if __name__ == '__main__':
    array = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    print(synmetric_check(array))
    for r in find_pair(array):
        print(r)




