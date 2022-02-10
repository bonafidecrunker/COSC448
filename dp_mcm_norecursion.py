import sys


class DpMCMNoRecursion:
    def __init__(self, arr):
        self.arr = arr
        n = len(arr) - 1
        self.m = [[0 for x in range(n)] for y in range(n)]
        self.s = [[0 for x in range(n)] for y in range(n)]
        self.in_a_result = [False for x in range(n)]

    def matrix_chain_order(self):
        n = len(self.arr) - 1
        for start in range(1, n):
            for i in range(0, n - start):
                j = i + start
                self.m[i][j] = sys.maxsize
                for k in range(i, j):
                    cost = self.m[i][k] + self.m[k + 1][j] + self.arr[i] * self.arr[k + 1] * self.arr[j + 1]
                    if cost < self.m[i][j]:
                        self.m[i][j] = cost
                        self.s[i][j] = k

    def print_optimal_parenthesizations(self):
        self.print_parenthesizations(0, len(self.s) - 1)

    def print_parenthesizations(self, i, j):
        if i != j:
            self.print_parenthesizations(i, self.s[i][j])
            self.print_parenthesizations(self.s[i][j] + 1, j)
            istr = "_result " if self.in_a_result[i] else " "
            jstr = "_result " if self.in_a_result[j] else " "
            print("A_" + str(i) + istr + "* A_" + str(j) + jstr)
            self.in_a_result[i] = True
            self.in_a_result[j] = True


def main():
    arr = [2, 3, 1, 3, 2, 3, 1]
    test = DpMCMNoRecursion(arr)
    test.matrix_chain_order()
    test.print_optimal_parenthesizations()


main()
exit(0)
