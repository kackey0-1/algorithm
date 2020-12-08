"""
Input: 'This is a pen. This is an apple. Applepen
Output: {'p', 6}
"""
from collections import Counter
import operator
from typing import Tuple


def find_char(chars: str) -> Tuple[str, int]:
    # myself
    cache = {}
    for char in chars.replace(' ', '').lower():
        if cache.get(char):
            cache[char] += 1
        else:
            cache[char] = 1
    w, tmax = '', 0
    for key, value in zip(cache.keys(), cache.values()):
        if tmax < value:
            w = key
            tmax = value
    return (w, tmax)


def count_chars_v1(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    l = []
    for char in strings:
        if not char.isspace():
            l.append((char, strings.count(char)))
    return max(l, key=operator.itemgetter(1))


def count_chars_v2(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    # l = []
    # for char in strings:
    #     if not char.isspace():
    #         l.append((char, strings.count(char)))
    l = [(c, strings.count(c)) for c in strings if not c.isspace()]
    return max(l, key=operator.itemgetter(1))


def count_chars_v3(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    # d = {}  # or dict()
    d = Counter()
    for char in strings:
        if not char.isspace():
            # d[char] = d.get(char, 0) + 1
            d[char] += 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


if __name__ == '__main__':
    chars = 'This is a pen. This is an apple. Applepen'
    print(find_char(chars))
    print(count_chars_v1(chars))
    print(count_chars_v2(chars))
    print(count_chars_v3(chars))
