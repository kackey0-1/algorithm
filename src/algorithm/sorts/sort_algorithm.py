"""
bucket_sort
"""

# select_sort
# 1. 未整列の配列から最も小さい数値を選択
# 2. 未整列の配列の先頭と最も小さい数値を交換
# 3. 繰り返し処理
def select_sort(arr):
    for i in range(0, len(arr)-1):
        select_min(i, arr)
def select_min(i, arr):
    min = i
    for j in range(i, len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]

# insert_sor
# 未ソート部分の一番左をtmpに入れる
# tmpの値がソート済みの配列においてtmpより小さい値を探し、挿入
# 繰り返す
def insert_sort(arr):
    for i in range(1, len(arr)):
        insert(i, arr)
def insert(i, arr):
    tmp = arr[i]
    for j in range(i -1, -1, -1):
        if arr[j] > tmp:
            arr[j + 1] = arr[j]
        else:
            arr[j + 1] = tmp
            break
    else:
        arr[0] = tmp

# bubble_sort
# 配列の一番後ろから隣通しを比較し、順番が逆なら交換
# 配列の個数-1分繰り返す
def bubble_sort(arr):
    for i in range(len(arr)-1):
        exchange(arr)
def exchange(arr):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]


# merge_sort
# 2つの配列に分割する
# 2つの配列をソートする
# 2つの配列をマージする
# 1. n個の要素を含む配列を、それぞれn/2個の要素を含む2つの部分配列に分割
# 2. その2つの部分配列をそれぞれmerge_sortでソート
# 3. 得られた2つのソート済み配列をmergeで統合
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
def merge(arrf, arrb):
    if len(arrf) < 1:
        return arrb
    if len(arrb) < 1:
        return arrf
    if arrf[0] <= arrb[0]:
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
    return quick_sort(left) + [p] + quick_sort(right)
def divide(p, arr):
    left = []
    right = []
    for i in range(len(arr)):
        if arr[i] < p:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return left, right

if __name__ == '__main__':
    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    print(org_list)
    select_sort(org_list)
    print(org_list)

    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    insert_sort(org_list)
    print(org_list)

    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    bubble_sort(org_list)
    print(org_list)

    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    print(merge_sort(org_list))
    print(quick_sort(org_list))
