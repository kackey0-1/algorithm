from typing import List
import random


def insert(nums: List) -> List:
    for i in range(1, len(nums)):
        temp = nums[i]
        for j in range(i, -1, -1):
            if nums[j-1] > temp:
                nums[j] = nums[j-1]
            else:
                break
        nums[j] = temp
        # print('temp: ' + str(temp) + ', j: ' + str(j))
        # print(nums)
    """Wrong Logic
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j-1] > nums[j]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    """
    return nums



if __name__ == '__main__':
    # arr = [random.randint(0, 100) for i in range(10)]
    arr = [4, 5, 9, 19, 1, 2]
    print(arr)
    print(insert(arr))
