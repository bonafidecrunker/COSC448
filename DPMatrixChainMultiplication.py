import sys


def chain_matrix_multiplication(matrices):
    def cols(i): return matrices[i][1]
    def rows(i): return matrices[i][0]

    n = len(matrices)

    # error catching if matrices cannot be multiplied due to mismatched dimensions
    for i in range(n - 1):
        if matrices[i][1] != matrices[i + 1][0]:
            raise RuntimeError('Matrices cannot be multiplied')

    f = {}

    for l in range(1, n + 1):
        for start in range(0, n - l + 1):
            # Base case
            if l == 1:
                f[(start, start)] = 0
                continue

            # Recursive case
            end = start + l - 1
            f[(start, end)] = min(f[(start, mid)] + f[(mid + 1, end)] + rows(start) * cols(mid) * cols(end) for mid in range(start, end))

    # returns minimum number of operations necessary
    # return f[(0, n - 1)]

    # returns dp matrix
    return f


test = [2, 10, 3, 8]
dp = [[-1 for i in range(len(test))] for j in range(len(test) - 1)]


def chain_matrix_multiplication_memoization(p, i, j):
    if i == j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = sys.maxsize

    for k in range(i, j):
        dp[i][j] = min(dp[i][j], chain_matrix_multiplication_memoization(p, i, k) + chain_matrix_multiplication_memoization(p, k + 1, j) + p[i - 1] * p[k] * p[j])

    return dp[i][j]


def matrix_chain_order(p, n):
    i = 1
    j = n - 1
    return chain_matrix_multiplication_memoization(p, i, j)


x = chain_matrix_multiplication([(2, 10), (10, 3), (3, 8)])
for key in x:
    print(str(key) + ": " + str(x[key]))
matrix_chain_order(test, len(test))
for row in range(len(dp)):
    print(dp[row])

exit(0)






