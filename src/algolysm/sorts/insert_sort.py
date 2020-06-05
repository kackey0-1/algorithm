# 擬似コード
"""
先頭の要素をソート済みとする
未ソート部分がなくなるまで以下の処理を繰り返す
1. 未ソート部分の先頭から要素を取り出しtmpに記録する
2. ソート済みの部分において、tmpよりも大きい要素を後方へ1つずつ移動する
3. 最後に空いた位置にtmpを挿入する
"""

# 挿入ソート
def insert_sort(arr):
    for i in range(1, len(arr)):
        insert(arr, i)

#[5, 3, 2]
def insert(arr, i):
    tmp = arr[i]                   # 未ソート要素の先頭を一時的なtmp変数に代入
    # range(startm stop, step)のように引数に整数を3つ指定すると、start ≦ i < stopでstepずつ増加する等差数列が生成される。
    for j in range(i - 1, -1, -1): #整列済みの要素を右から順に
        if tmp < arr[j]:           #整列済みの要素が大きいなら
            arr[j + 1] = arr[j]    #後方へ1つ移動
        else:
            arr[j + 1] = tmp       #挿入位置決定
            break                  #比較終了
    else:                          #どの整理済み要素よりも小さいなら
        arr[0] = tmp               #一番左に挿入

if __name__ == '__main__':
    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    insert_sort(org_list)
    print(org_list)
