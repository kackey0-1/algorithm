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
    cache = set()
    l = []
    for data in array:
        cache.add((data[1], data[0]))
        if data in cache:
            l.append(data)
    return l


def count_max_v1(strings: str) -> Tuple[int, int]:
    """
    Input: 'This is a pen. This is an apple. Applepen
    Output: ('p', 6)
    """
    strings = strings.lower()
    count = dict()
    for char in strings:
        if not char.isspace():
            count[char] = count.get(char, 0) + 1
    max_key = max(count, key=count.get)
    return max_key, count[max_key]



def count_max_v2(strings: str) -> Tuple[int, int]:
    """
    Input: 'This is a pen. This is an apple. Applepen
    Output: ('p', 6)
    """
    strings = strings.lower()
    counter = Counter()
    for s in strings:
        if not s.isspace():
            counter[s] += 1
    max_key = max(counter, key=counter.get)
    return max_key, counter[max_key]


def count_max_v3(strings: str) -> Tuple[int, int]:
    """
    Input: 'This is a pen. This is an apple. Applepen
    Output: ('p', 6)
    """
    strings = strings.lower()
    l = [(s, strings.count(s)) for s in strings if not s.isspace()]
    return max(l, key=operator.itemgetter(1))


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
    x_count = Counter(x)
    y_count = Counter(y)
    # print(x_count)
    # print(y_count)
    for x_key, x_value in x_count.items():
        y_value = y_count.get(x_key)
        if y_value:
            if x_value < y_value:
                x[:] = [_ for _ in x if _ != x_key]
            elif x_value > y_value:
                y[:] = [_ for _ in y if _ != x_key]
    return x, y

if __name__ == '__main__':
    l = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    print(synmetric(l))

    strings = 'This is a pen. This is an apple. Applepen'
    print(count_max_v1(strings))
    print(count_max_v2(strings))
    print(count_max_v3(strings))
    #
    x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    y = [4, 5, 5, 5, 6, 7, 8, 8, 18]
    print('x = ', x)
    print('y = ', y)
    min_count_remove(x, y)
    print('x = ', x)
    print('y = ', y)
    #
    # for i in range(10):
    #     print(long_func(i))
    # print('#' * 100)
    # start = time.time()
    # for i in range(10):
    #     print(long_func(i))
    # print(start - time.time())


















