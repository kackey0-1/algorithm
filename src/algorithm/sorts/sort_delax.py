import random

"""
select_sort
insert_sort
bubble_sort
merge_sort
quick_sort
"""


def create_arr(n=30):
    arr = []
    for i in range(n):
        arr.append(random.randrange(n))
    return arr


def select_sort(arr):
    for i in range(len(arr) - 1):
        select_min(i, arr)


def select_min(i, arr):
    min = i
    for j in range(i, len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]

def insert_sort(arr):
    for i in range(1, len(arr)):
        insert(i, arr)

def insert(i, arr):
    tmp = arr[i]
    for j in range(i - 1, -1, -1):
        if tmp < arr[j]:
            arr[i + 1] = arr[j]
        else:
            arr[i + 1] = tmp
            break
    else:
        arr[0] = tmp

if __name__ == '__main__':
    select_list = create_arr()
    select_sort(select_list)
    print(select_list)

    insert_list = create_arr()
    insert_sort(insert_list)
    print(insert_list)