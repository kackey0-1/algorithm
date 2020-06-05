# 擬似コード
"""
順番が逆なっている隣接要素がなくなるまで以下の処理を繰り返す
1. 配列の末尾から隣接する要素を順番に比べていき、大小関係が逆ならば変換する
"""

# バブルソート
def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        exchange(arr, i)

def exchange(arr, i):
    for j in range(len(arr)-1, i, -1):          #リストの末尾から順番に
        if arr[j-1] > arr[j]:                   #要素を比較して大小関係が逆なら
            arr[j-1], arr[j] = arr[j], arr[j-1] #位置を交換する

if __name__ == '__main__':
    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    bubble_sort(org_list)
    print(org_list)
