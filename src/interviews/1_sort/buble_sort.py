from typing import List
import random


def buble(nums: List) -> List:
    for i in range(len(nums)):
        for j in range(len(nums) -1):
            # print(nums[j], nums[j + 1])
            if nums[j] > nums[j+1]:
                # print(nums)
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == '__main__':
    # numbers = [1, 8, 3, 5, 2, 9, 4]
    numbers = [random.randint(1, 100) for i in range(100)]
    print(numbers)
    print(buble(numbers))
