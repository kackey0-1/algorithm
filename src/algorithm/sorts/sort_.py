import random


def create_arr(n=30):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, n))
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
            arr[j + 1] = arr[j]
        else:
            arr[j + 1] = tmp
            break
    else:
        arr[0] = tmp


def bubble_sort(arr):
    for i in range(len(arr)):
        exchange(arr)


def exchange(arr):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    # select sort
    select_list = create_arr()
    print(select_list)
    select_sort(select_list)
    print(select_list)

    # insert sort
    insert_list = create_arr()
    print(insert_list)
    insert_sort(insert_list)
    print(insert_list)

    # bubble sort
    bubble_list = create_arr()
    print(bubble_list)
    bubble_sort(bubble_list)
    print(bubble_list)
