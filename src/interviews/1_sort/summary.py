from typing import List
import random


def quick(numbers: List[int]) -> None:
    def _sort(numbers: List[int], low: int, high: int) -> None:
        if not low < high:
            return
        partition_index = partition(numbers, low, high)
        _sort(numbers, low, partition_index - 1)
        _sort(numbers, partition_index, high)
    _sort(numbers, 0, len(numbers) - 1)


def partition(numbers: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1


def select(numbers: List[int]) -> None:
    length = len(numbers)
    for i in range(length):
        tmin = i
        for j in range(i, length):
            if numbers[j] < numbers[tmin]:
                tmin = j
        numbers[i], numbers[tmin] = numbers[tmin], numbers[i]


def bubble(numbers: List[int]) -> None:
    length = len(numbers)
    for i in range(length):
        for j in range(length):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]


def insert(numbers: List[int]) -> None:
    length = len(numbers)
    for i in range(length):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp


def merge(numbers: List[int]):
    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2
    left = numbers[center:]
    right = numbers[:center]

    merge(left)
    merge(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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


if __name__ == '__main__':
    print('##### Bubble Sort #####')
    numbers = [random.randint(0, 100) for i in range(10)]
    print(numbers)
    bubble(numbers)
    print(numbers)

    print('##### Select Sort #####')
    numbers = [random.randint(0, 100) for i in range(10)]
    print(numbers)
    select(numbers)
    print(numbers)

    print('##### Insert Sort #####' )
    numbers = [random.randint(0, 100) for i in range(10)]
    print(numbers)
    insert(numbers)
    print(numbers)

    print('##### Quick Sort #####')
    numbers = [random.randint(0, 100) for i in range(10)]
    print(numbers)
    quick(numbers)
    print(numbers)

    print('##### Merge Sort #####')
    numbers = [random.randint(0, 100) for i in range(10)]
    print(numbers)
    merge(numbers)
    print(numbers)









