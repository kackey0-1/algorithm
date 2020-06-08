# 疑似コード
"""
1. n個の要素を含む配列を、それぞれn/2個の要素を含む2つの部分配列に分割
2. その2つの部分配列をそれぞれmerge_sortでソート
3. 得られた2つのソート済み配列をmergeで統合
"""

# 分割
def merge_sort(arr):
    # 再帰呼び出しの終了
    if len(arr) < 2:
        return arr
    # 配列の真ん中を求める(//=小数点以下切り捨て)
    mid = len(arr) // 2
    # 配列を分割
    # print(arr)
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

# マージ(前の配列, 後の配列)
def merge(arrf, arrb):
    if len(arrf) < 1:
        return arrb
    if len(arrb) < 1:
        return arrf
    
    # 先頭要素を比較して小さい方を先頭に配置 
    if arrf[0] <= arrb[0]:
        # 前の配列の先頭要素 前の配列の先頭要素以下 後ろのほうの配列をマージ
        return [arrf[0]] + merge(arrf[1:], arrb)
    else:
        # 後の配列の先頭要素 前のほうの配列をマージ 後ろのほうの先頭要素以下の配列をマージ
        return [arrb[0]] + merge(arrf, arrb[1:])

if __name__ == '__main__':
    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    print(merge_sort(org_list))
    # マージソートは新しい配列を返す関数のため最初のorg_listは当初のままとなる
    print(org_list)
