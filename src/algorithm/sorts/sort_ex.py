import random

"""
merge_sort
quick_sort
"""
def create_arr(n=30):
    arr = []
    for i in range(n):
        arr.append(random.randrange(n))
    return arr

def select_sort(arr):
    for i in range(len(arr)-1):
        select_min(i, arr)
def select_min(i, arr):
    min = arr[i]
    for j in range(i, len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]

def insert_sort(arr):
    for i in range(len(arr)):
        # iは未整列の先頭位置を示すindex
        insert(i, arr)
def insert(i, arr):
    tmp = arr[i]
    for j in range(i-1, -1, -1):
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
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

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
"""
quick_sort
1. ソート対象の配列をピポット(=分割の基準)を基準に2つの部分配列に分割(divide)
2. 前方の部分配列に対してquick_sortを行う(solve)
3. 後方の部分配列に対してquick_sortを行う(solve)
4. 整列済み部分配列とピボットを連結して返す(Conquer)
"""
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
    # select_sort
    print(f'{"#" * 10} Select Sort {"#" * 10}')
    select_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    print(select_list)
    select_sort(select_list)
    print(select_list)
    # insert_sort
    print(f'{"#" * 10} Insert Sort {"#" * 10}')
    insert_list = create_arr()
    print(insert_list)
    insert_sort(insert_list)
    print(insert_list)
    # bubble_sort
    print(f'{"#" * 10} Bubble Sort {"#" * 10}')
    bubble_list = create_arr()
    print(bubble_list)
    bubble_sort(bubble_list)
    print(bubble_list)
    # merge_sort
    print(f'{"#" * 10} Merge Sort {"#" * 10}')
    merge_list = create_arr()
    print(merge_list)
    print(merge_sort(merge_list))
    # quick_sort
    print(f'{"#" * 10} Quick Sort {"#" * 10}')
    quick_list = create_arr()
    print(quick_list)
    print(quick_sort(quick_list))
