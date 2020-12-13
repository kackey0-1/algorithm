"""
[1] => [2] => 2
[2, 3] => [2, 4] => 24
[8, 9] => [9, 0] => 90
[9, 9] => [1, 0, 0] => 100
[1, 2, 3] => [1, 2, 4] => 124
[7, 8, 9] => [7, 9, 0] => 790
[9, 9, 9] => [1, 0, 0, 0] => 1000
[9, 9, 9, 9] => [1, 0, 0, 0, 0] => 10000
[0, 0, 0, 9, 9, 9, 9] => [1, 0, 0, 0] => 10000
"""

from typing import List


def add(numbers: List[int]) -> List[int]:
    strings = ''
    for n in numbers:
        strings += str(n)
    strings = str(int(strings) + 1)
    # return [int(s) for s in strings]
    return list(map(int, strings))


def summary(numbers: List[int]) -> int:
    strings = ''
    for n in numbers:
        strings += str(n)
    return int(strings)


if __name__ == '__main__':
    print(summary(add([1])))
    print(summary(add([2, 3])))
    print(summary(add([8, 9])))
    print(summary(add([9, 9])))
    print(summary(add([1, 2, 3])))
    print(summary(add([7, 8, 9])))
    print(summary(add([9, 9, 9])))
    print(summary(add([9, 9, 9, 9])))
    print(summary(add([0, 0, 0, 9, 9, 9, 9])))
