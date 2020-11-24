from typing import List
import random


def merge(nums: List) -> List:
    if len(nums) <= 1:
        return nums

    center = len(nums) // 2
    left = nums[:center]
    right = nums[center:]

    merge(left)
    merge(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums


if __name__ == '__main__':
    numbers = [random.randint(0, 100) for i in range(10)]
    print(numbers)
    print(merge(numbers))








