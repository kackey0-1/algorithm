from typing import List
import random


def partition(numbers: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] < pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

    return i+1


def quick(nums: List) -> List:
    def _quick_sort(numbers: List, low: int, high: int):
        partition_index = partition(numbers, low, high)
        _quick_sort(numbers, partition_index+1, high)
        _quick_sort(numbers, low, partition_index-1)
    _quick_sort(nums, 0, len(nums)-1)
    return nums


if __name__ == '__main__':
    numbers = [random.randint(0, 100) for i in range(10)]
    print(numbers)
    print(quick(numbers))








