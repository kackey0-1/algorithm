def _self_fibonacci(n):
    prev_a = 0
    prev_b = 0
    fibo = []
    for i in range(0, n):
        if i == 0 or i == 1:
            fibo.append(1)
        else:
            fibo.append(prev_a + prev_b)
        prev_a = prev_b
        prev_b = fibo[i]
    return fibo


def _self_fibonacci_ex(n):
    # n = n-1
    fibo = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
            46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465]
    if n == 0:
        return fibo[0]
    if n == 1:
        return fibo[1]
    return fibo[n - 2] + fibo[n - 1]


# フィボナッチ数列(分割統治法)
# しかし、無駄な計算が多い
# 同じ計算が何度もされるため相性悪い
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# フィボナッチ数列(動的計画法1)
def fib_mem(n):
    # 予めメモリ領域を確保
    mem = [None] * (n + 1)

    def _fib(n):
        if n == 0 or n == 1:
            return 1
        if mem[n] != None:
            return mem[n]
        mem[n] = _fib(n - 1) + _fib(n - 2)
        return mem[n]

    return _fib(n)


# フィボナッチ数列(動的計画法2)
def fib_dp(n):
    mem = [None] * n
    mem[0] = 1
    mem[1] = 1
    for i in range(2, n):
        mem[i] = mem[i - 2] + mem[i - 1]
    return mem


if __name__ == '__main__':
    # fibo = _self_fibonacci(34)
    # print(fibo)
    # print(len(fibo))
    # print(_self_fibonacci_ex(35))
    # for j in range(0, 35):
    # print(fib(35))
    print(fib_mem(35))
    print(fib_dp(35))
