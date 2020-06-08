"""
N を 2 以上の整数とし、N の約数のうち N 自身を除いたものの和を S とします。 このとき
・N = S となるような N を完全数
・|N-S| = 1 となるような N をほぼ完全数
と言うことにしましょう。ここで、|N-S| は N-S の絶対値を意味します。
たとえば、N = 28 のとき、28 の約数は 1, 2, 4, 7, 14, 28 なので、S = 1+2+4+7+14 = 28 となります。従って、28 は完全数です。
また、N = 16 のときには S = 1+2+4+8 = 15 となるので、16 はほぼ完全数です。
入力された整数が完全数かほぼ完全数かそのいずれでもないかを判定するプログラムを作成してください。

# 条件
すべてのテストケースで以下の条件を満たします。
・1 ≦ Q ≦ 50
・2 ≦ N_i ≦ 1000 (i=1, 2, ..., Q)

# 入力例1
3
28
16
777

# 出力例1
perfect
nearly
neither

# アプローチの手順
1. 約数を求める関数作成
2. 完全数、ほぼ完全数、not完全数かを判定する関数作成
3. 入力値ごとに処理をするループ処理作成
"""
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def dividers(n):
    dividable_nums = []
    for i in range(n):
        i += 1
        if n%i == 0:
            dividable_nums.append(i)
        else:
            continue
    return dividable_nums

def is_valid(n, dividable_nums):
    total = 0
    for i in dividable_nums:
        if i==n:
            continue
        else:
            total += i
    if n-total==0:
        return 'perfect'
    elif abs(n-total)==1:
        return 'nearly'
    else:
        return 'neither'

# n1 = 28
# print(is_valid(n1, dividers(n1)))
# n2 = 16
# print(is_valid(n2, dividers(n2)))
# n3 = 777
# print(is_valid(n3, dividers(n3)))
# n4 = 3
# print(is_valid(n4, dividers(n4)))
# n5 = 4
# print(is_valid(n5, dividers(n5)))
# n6 = 5
# print(is_valid(n6, dividers(n5)))
# n7 = 6
# print(is_valid(n7, dividers(n7)))


loop_count = int(input())
for in range(loop_count):
    n = int(input())
    print(n, dividers(n))

