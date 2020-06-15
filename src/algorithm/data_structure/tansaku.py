"""
データ構造:
    データの集合の
    1. 格納規則
    2. 操作方法
    を決定するもの
    問題の性質に

探索: データの集合から目的の要素を探し出す処理
配列 [1,2,5,8,10]において、ランダムに選択される数字n (nは1以上10以下の整数)が
配列に含まれる場合はその位置を、含まれない場合はNoneを返すプログラムを作成

線形探索:
先頭から順番に値を確認

二分探索:
探索範囲を半分に絞っていく探索(ソート済みの配列のみに利用可能)
真ん中(mid)の要素と比較したい値を比較
"""
import random


def pprint(method, n=25):
    print(f'{"#" * n} {method} {"#" * n}')


def create_arr():
    arr = []
    n = 10
    for i in range(n):
        arr.append(random.randint(1, n))
    print(arr)
    return quick_sort(arr)


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    p = arr[0]
    left, right = divide(p, arr[1:])
    return quick_sort(left) + [p] + quick_sort(right)


def divide(p, arr):
    left, right = [], []
    for n in arr:
        if p > n:
            left.append(n)
        else:
            right.append(n)
    return left, right


def liner_search(target, arr):
    """線形探索"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None


# def include_2(target, arr):
#     """二分探索(ソート済みの場合のみ利用可能)"""
#     index = None
#     mid = len(arr) // 2
#     divided_arr = divide(mid, arr)
#     for i in range(len(divided_arr)):
#         if divided_arr[i] == target:
#             index = i
#             if arr[mid] <= target:
#                 index += mid
#     return index
#
#
# def divide(mid, arr):
#     if arr[mid] > target:
#         return arr[:mid]
#     else:
#         return arr[mid:]


def binary_search(target, arr):
    """二分探索(ソート済みの場合のみ利用可能)"""
    left = 0
    right = len(arr)
    while left < right:
        print(left, right)
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        # 真ん中の要素が探している要素より大きい場合、小さい範囲の配列インデックスを無視
        elif arr[mid] > target:
            right = mid
        # 真ん中の要素が探している要素と等しいもしくは小さい場合、大きい範囲の配列インデックスを無視
        else:
            left = mid + 1
    return None


if __name__ == '__main__':
    nums = create_arr()
    target = random.randint(1, 10)
    # target = 5
    print(nums)
    print(f'{target} が含まれるかを確認')

    pprint("linear_search")
    print(liner_search(target, nums))

    # pprint("include_2")
    # print(include_2(target, nums))

    pprint("binary_search")
    print(binary_search(target, nums))
