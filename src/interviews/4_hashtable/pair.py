"""
1. Input: [11, 2, 5, 9, 10, 3], 12 => Output: (2, 10) or None
2. Input: [11, 2, 5, 9, 10, 3]     => Output: (11, 9) or None ex) 11 + 9 = 2 + 5 + 10 + 3
"""

from typing import Optional, List


def get_pair(numbers: List[int], value: int) -> Optional[tuple]:
    cache = set()
    for n in numbers:
        cache.add(n)
        val = value - n
        if val in cache:
            return val, n


def get_pair_half_sum(numbers: List[int]) -> Optional[int]:
    total = sum(numbers)
    cache = set()
    half, remainder = divmod(total, 2)
    if remainder != 0:
        return
    for n in numbers:
        cache.add(n)
        val = half - n
        if val in cache:
            return val, n
    """
    total = sum(numbers)
    for x in numbers:
        for y in numbers:
            if x == y:
                continue
            if total / (x + y) == 2:
                return x, y
    """


if __name__ == '__main__':
    numbers = [11, 2, 5, 9, 10, 3]
    target = 12
    print(get_pair(numbers, target))
    print(get_pair_half_sum(numbers))
