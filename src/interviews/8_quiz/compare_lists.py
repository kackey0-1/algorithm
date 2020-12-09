"""
Input:  X: [1, 2, 3, 4, 4, 5, 5, 8, 10] Y: [4, 5, 5, 5, 6, 7, 8, 8, 18]
Output: X: [1, 2, 3, 4, 4, 10] Y: [5, 5, 5, 6, 7, 8, 8, 18]
"""
from typing import List
from collections import Counter


def compaire(list1: List[int], list2: List[int]):
    cache = list1
    for v in cache:
        c1 = list1.count(v)
        c2 = list2.count(v)
        if c2 > c1 != 0:
            for i in range(c1):
                list1.remove(v)
        elif c1 > c2 != 0:
            for i in range(c2):
                list2.remove(v)
    return list1, list2


def min_count_remove(x: List[int], y: List[int]):
    # count_x = {}
    # count_y = {}
    # for i in x:
    #     count_x[i] = count_x.get(i, 0) + 1
    # for i in y:
    #     count_y[i] = count_y.get(i, 0) + 1
    # print(count_x)
    # print(count_y)
    counter_x = Counter(x)
    counter_y = Counter(y)
    for key_x, value_x in counter_x.items():
        value_y = counter_y.get(key_x)
        if value_y:
            if value_x < value_y:
                x[:] = [i for i in x if i != key_x]
            elif value_x > value_y:
                y[:] = [i for i in y if i != key_x]


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    list2 = [4, 5, 5, 5, 6, 7, 8, 8, 18]
    # print(compaire(list1, list2))
    print('x = ', list1)
    print('y = ', list2)
    min_count_remove(list1, list2)
    print('x = ', list1)
    print('y = ', list2)



