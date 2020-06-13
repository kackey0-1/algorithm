import random


def create_arr(n=30):
    arr = []
    for i in range(n):
        arr.append(random.randrange(n))
    return arr


def pprint(method, n=25):
    print(f'{"#" * n} {method} {"#" * n}')


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
    for i in range(len(arr) - 1):
        exchange(arr)


def exchange(arr):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge(arrf, arrb):
    if len(arrf) == 0:
        return arrb
    if len(arrb) == 0:
        return arrf
    if arrf[0] < arrb[0]:
        return [arrf[0]] + merge(arrf[1:], arrb)
    else:
        return [arrb[0]] + merge(arrf, arrb[1:])


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    p = arr[0]
    left, right = divide(p, arr[1:])
    # print(left, right)
    return quick_sort(left) + [p] + quick_sort(right)


def divide(p, arr):
    left = []
    right = []
    for n in arr:
        if p > n:
            left.append(n)
        else:
            right.append(n)
    return left, right


if __name__ == '__main__':
    """
    select_sort
    insert_sort
    bubble_sort
    merge_sort
    quick_sort
    """
    pprint("select_sort")
    select_list = create_arr()
    print(select_list)
    select_sort(select_list)
    print(select_list)
    print(len(select_list))

    pprint("insert_sort")
    insert_list = create_arr()
    print(insert_list)
    insert_sort(insert_list)
    print(insert_list)
    print(len(insert_list))

    pprint("bubble_sort")
    bubble_list = create_arr()
    print(bubble_list)
    bubble_sort(bubble_list)
    print(bubble_list)
    print(len(bubble_list))

    pprint("merge_sort")
    merge_list = create_arr()
    print(merge_list)
    insert_sort(merge_list)
    print(merge_list)
    print(len(merge_list))

    pprint("quick_sort")
    quick_list = create_arr()
    print(quick_list)
    print(quick_sort(quick_list))
    print(len(quick_list))
