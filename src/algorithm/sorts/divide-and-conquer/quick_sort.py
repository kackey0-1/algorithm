# 擬似コード(クイックソート)
"""
1. ソート対象の配列をピポット(=分割の基準)を基準に2つの部分配列に分割(divide)
2. 前方の部分配列に対してquick_sortを行う(solve)
3. 後方の部分配列に対してquick_sortを行う(solve)
4. 整列済み部分配列とピボットを連結して返す(Conquer)
"""
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    # ピボットの設定
    p = arr[0]
    arrf, arrb = divide(p, arr[1:])
    # ピボットを基準に左右ソートさせて連結させることでソートされた配列となる
    print(f'{"#"*30}')
    print('array', arr)
    print('array_forward', arrf)
    print('array_back', arrb)
    print(f'{"#"*30}')
    return quick_sort(arrf) + [p] + quick_sort(arrb)

# ピボットを基準に分割
def divide(p, arr):
    left = []
    right = []
    for i in arr:
        if i < p:
            left.append(i)
        else:
            right.append(i)
    return left, right



if __name__ == '__main__':
    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    print(org_list)
    print(quick_sort(org_list))
