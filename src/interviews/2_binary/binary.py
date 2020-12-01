from typing import List, NewType
import random


IndexNum = NewType('IndexNum', int)


def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
            k += 1
        else:
            numbers[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1
    return numbers


def binary_iterative(sorted_numbers: List[int], value: IndexNum) -> IndexNum:
    left = 0
    right = len(sorted_numbers)
    while left <= right:
        mid = (left + right) // 2
        if sorted_numbers[mid] == value:
            return mid
        elif sorted_numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    # numbers = [random.randint(0, 100) for i in range(10)]
    numbers = [20, 91, 39, 16, 12, 7, 19, 88, 69, 28]
    print(numbers)
    sorted_numbers = merge_sort(numbers)
    print(sorted_numbers)
    print(binary_iterative(numbers, 20))

