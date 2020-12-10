from typing import List, Tuple
from collections import Counter
import operator
import time


def synmetric(array: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Synmetric
    Input [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    Output [(5, 3), (7, 4)]
    """
    cache = {}
    l = []
    for n in array:
        left = n[0]
        right = n[1]
        cache[right] = left
        if right == cache.get(left):
            l.append(n)
    return l


def count_max_v1(strings: str) -> Tuple[int, int]:
    """
    Input: 'This is a pen. This is an apple. Applepen
    Output: ('p', 6)
    """
    strings = strings.lower()
    counter = Counter()
    for char in strings:
        if not char.isspace():
            counter[char] += 1
    max_key = max(counter, key=counter.get)
    return (max_key, counter[max_key])


def count_max_v2(strings: str) -> Tuple[int, int]:
    """
    Input: 'This is a pen. This is an apple. Applepen
    Output: ('p', 6)
    """
    strings = strings.lower()
    l = [(c, strings.count(c)) for c in strings if not c.isspace()]
    return max(l, key=operator.itemgetter(1))


def count_max_v3(strings: str) -> Tuple[int, int]:
    """
    Input: 'This is a pen. This is an apple. Applepen
    Output: ('p', 6)
    """
    d = {}
    strings = strings.lower()
    for char in strings:
        if not char.isspace():
            d[char] = strings.count(char)
    max_key = max(d, key=d.get)
    return (max_key, d[max_key])


def memorize(f):
    """
    Implements decorator to cache func
    """
    cache = {}

    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return _wrapper


@memorize
def long_func(n: int):
    r = 0
    for i in range(10000000):
        r += n * i
    return r


def min_count_remove(x: List[int], y: List[int]) -> None:
    """
    Input:  X: [1, 2, 3, 4, 4, 5, 5, 8, 10] Y: [4, 5, 5, 5, 6, 7, 8, 8, 18]
    Output: X: [1, 2, 3, 4, 4, 10] Y: [5, 5, 5, 6, 7, 8, 8, 18]
    """
    count_x = Counter(x)
    count_y = Counter(y)
    for key_x, value_x in count_x.items():
        value_y = count_y[key_x]
        if value_y:
            if value_x < value_y:
                x[:] = [i for i in x if i != key_x]
            elif value_x > value_y:
                y[:] = [i for i in y if i != key_x]


if __name__ == '__main__':
    l = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    print(synmetric(l))

    strings = 'This is a pen. This is an apple. Applepen'
    print(count_max_v1(strings))
    print(count_max_v2(strings))
    print(count_max_v3(strings))

    x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    y = [4, 5, 5, 5, 6, 7, 8, 8, 18]
    print('x = ', x)
    print('y = ', y)
    min_count_remove(x, y)
    print('x = ', x)
    print('y = ', y)

    for i in range(10):
        print(long_func(i))
    print('#' * 100)
    start = time.time()
    for i in range(10):
        print(long_func(i))
    print(start - time.time())


