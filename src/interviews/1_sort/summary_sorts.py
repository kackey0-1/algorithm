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









