from typing import List
import random


def bubble_sort(numbers: List[int]):
    for i in range(1, len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]


def select_sort(numbers: List[int]):
    for i in range(len(numbers)):
        tmin = i
        for j in range(i, len(numbers)):
            if numbers[tmin] > numbers[j]:
                tmin = j
        numbers[i], numbers[tmin] = numbers[tmin], numbers[i]


def insert_sort(numbers: List[int]):
    # TODO do it again
    for i in range(1, len(numbers)):
        temp = numbers[i]
        for j in range(i, -1, -1):
            if numbers[j-1] > temp:
                numbers[j] = numbers[j-1]
            else:
                break
        numbers[j] = temp


def merge_sort(numbers: List[int]):
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


def quick_sort(numbers: List[int]):
    def _sort(numbers: List[int], low: int, high: int):
        if low < high:
            partition_index = partition(numbers, low, high)
            _sort(numbers, partition_index, high)
            _sort(numbers, low, partition_index - 1)
    _sort(numbers, 0, len(numbers)-1)


def partition(numbers: List[int], low: int, high: int):
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1


if __name__ == '__main__':
    numbers = [random.randint(0, 100) for i in range(10)]
    print(numbers)
    bubble_sort(numbers)
    print(numbers)

    numbers = [random.randint(0, 100) for i in range(10)]
    print(numbers)
    select_sort(numbers)
    print(numbers)

    numbers = [random.randint(0, 100) for i in range(10)]
    print(numbers)
    insert_sort(numbers)
    print(numbers)

    numbers = [random.randint(0, 100) for i in range(10)]
    print(numbers)
    merge_sort(numbers)
    print(numbers)

    numbers = [random.randint(0, 100) for i in range(10)]
    print(numbers)
    quick_sort(numbers)
    print(numbers)





