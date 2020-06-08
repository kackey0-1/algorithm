# 擬似コード(選択ソート)
"""
以下の操作を配列の要素数-1回繰り返す
1. 未ソート部分から最小の要素の位置minを特定する
2. minの位置にある要素と未ソートの部分の先頭要素を交換
"""

# 選択ソート
def select_sort(arr):
    for i in range(0, len(arr)-1):
        select_min(arr, i)

def select_min(arr, i):
    # 最小要素の位置の特定
    min = i
    for j in range(i + 1, len(arr)):
        if arr[min] > arr[j]:
            min = j
    # 最小要素と先頭要素を交換
    arr[i], arr[min] = arr[min], arr[i]

if __name__ == '__main__':
    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    select_sort(org_list)
    print(org_list)
