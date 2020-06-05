
"""
ソート手法
1. 選択ソート: 最小値を見つけて新規配列の末尾に追加していく手法
2. 挿入ソート: 整列済み要素に挿入していく手法
3. バブルソート: 隣り合う要素を比較・交換
"""

##############################################################
# 1. 選択ソート: 最小値を見つけて新規配列の末尾に追加していく手法
def select_sort(arr):
    for i in range(len(arr)-1):
        select_min(i, arr)
# リストから最小値を返す
def select_min(i, arr):
    min = i
    for j in range(i, len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]
##############################################################

##############################################################
# 2. 挿入ソート: 未整列の要素から順に整列済み要素に挿入していく手法
# もう一度書くこと
def insert_sort(arr):
    for i in range(1, len(arr)):
        insert(i, arr)
#[5,4]
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
##############################################################

##############################################################
# 3. バブルソート: 隣り合う要素を比較・交換
def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        exchange(i, arr)
#[5,4]
def exchange(i, arr):
    for j in range(len(arr)-1, i, -1):
        if arr[j] < arr[j-1]:
            arr[j] ,arr[j-1]  = arr[j-1], arr[j]

##############################################################
if __name__ == '__main__':
    # 選択ソート
    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    print(org_list)
    select_sort(org_list)
    print(org_list)
    # 挿入ソート
    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    insert_sort(org_list)
    print(org_list)
    # バブルソート
    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    bubble_sort(org_list)
    print(org_list)