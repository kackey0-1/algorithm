from typing import List, NewType
import random


IndexNum = NewType('IndexNum', int)


def liner_search(sorted_numbers: List[int], value: int) -> IndexNum:
    for i in range(len(sorted_numbers)):
        if sorted_numbers[i] == value:
            return i
    return -1


def binary_search(sorted_numbers: List[int], value: int) -> IndexNum:
    left = 0
    right = len(sorted_numbers)
    while left <= right:
        middle = (left + right) // 2
        if value == sorted_numbers[middle]:
            return middle
        elif value > sorted_numbers[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def binary_search_recursive(sorted_numbers: List[int], value: int) -> IndexNum:
    def _binary_search(numbers: List[int], value: int,
                       left: IndexNum, right: IndexNum) -> IndexNum:
        if left > right:
            return -1
        mid = (left + right) // 2
        if value == numbers[mid]:
            return mid
        elif value < numbers[mid]:
            return _binary_search(numbers, value, left, mid-1)
        else:
            return _binary_search(numbers, value, mid+1, right)
    return _binary_search(sorted_numbers, value, 0, len(sorted_numbers)-1)


if __name__ == '__main__':
    numbers = [random.randint(0, 100) for i in range(10)]
    numbers = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    print(numbers)
    print(liner_search(numbers, 15))

    print(numbers)
    print(binary_search(numbers, 20))
    print(numbers)
    print(binary_search_recursive(numbers, 20))

