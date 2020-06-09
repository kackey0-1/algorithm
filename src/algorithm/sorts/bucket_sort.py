
def bucket_sort(arr):
    # ソート対象の配列の最大要素が収まるカウンタ配列を用意
    arrc = [0] * (max(arr)+1)
    # 要素の数をカウント
    for i in arr:
        arrc[i] += 1
    # 累積和を求める
    for j in range(1, len(arrc)):
        arrc[j] = arrc[j] + arrc[j-1]
    # ソート先配列を用意して代入していく
    arrs = [0] * len(arr)
    for i in reversed(arr):
        # カウンタ配列の指定先が1始まりなので、-1して調整
        arrs[arrc[i]-1] = i
        arrc[i] -= 1
    return arrs

if __name__ == '__main__':
    org_list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]
    print(org_list)
    print(bucket_sort(org_list))


