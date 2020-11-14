from typing import List
import random


def select(nums: List) -> List:
    for i in range(len(nums)):
        tmin = i
        for j in range(i, len(nums)):
            if arr[tmin] > arr[j]:
                tmin = j
        arr[i], arr[tmin] = arr[tmin], arr[i]
    return nums


if __name__ == '__main__':
    arr = [random.randint(0, 100) for i in range(10)]
    print(arr)
    print(select(arr))

