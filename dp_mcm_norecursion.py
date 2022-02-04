import sys


class DpMCMNoRecursion:
    def __init__(self, m, s, in_a_result, arr):
        self.m = m
        self.s = s
        self.in_a_result = [False for i in range(len(arr))]
        self.arr = arr

    def matrix_chain_order(self, dimensions):
        n = len(dimensions) - 1
        m = [[0 for i in range(n)] for j in range(n)]
        s = [[0 for i in range(n)] for j in range(n)]

        for start in range(1, n):
            for i in range(n - start):
                j = i + start
                m[i][j] = sys.maxsize
                for k in range(i, j):
                    cost = m[i][k] + m[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                    if cost < m[i][j]:
                        m[i][j] = cost
                        s[i][j] = k

    def print_optimal_parenthesizations(self):
        in_a_result = [False for i in range(len(self.s))]
        self.print_parenthesizations(self.s, 0, len(self.s) - 1, in_a_result)

    def print_parenthesizations(self, s, i, j, in_a_result):
        if i != j:
            self.print_parenthesizations(s, i, s[i][j], in_a_result)
            self.print_parenthesizations(s, s[i][j] + 1, j, in_a_result)
            istr = "_result " if in_a_result[i] else " "
            jstr = "_result " if in_a_result[j] else " "
            print(" A_" + str(i) + istr + "* A_" + str(j) + jstr)
            in_a_result[i] = True
            in_a_result[j] = True


def main():
    arr = [2, 10, 3, 8]
    m, s = [[0 for i in range(len(arr))] for j in range(len(arr))], [[0 for i in range(len(arr))] for j in range(len(arr))]
    in_a_result = [False for i in range(len(arr))]
    test = DpMCMNoRecursion(m, s, in_a_result, arr)
    test.matrix_chain_order(arr)
    test.print_optimal_parenthesizations()


main()
exit(0)
