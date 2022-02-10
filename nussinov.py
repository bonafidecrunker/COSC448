import numpy as np
import pandas as pd

minimum_loop_length = 4


def pair(t):
    return 1 if t in [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')] else 0


def dot_write(seq, fold):
    dot = ['.' for i in range(len(seq))]
    for s in fold:
        dot[min(s)] = '('
        dot[max(s)] = ')'
    return ''.join(dot)


def traceback(dp, seq, fold, i, L):
    j = L
    if i < j:
        if dp[i][j] == dp[i + 1][j]:
            traceback(dp, seq, fold, i + 1, j)
        elif dp[i][j] == dp[i][j - 1]:
            traceback(dp, seq, fold, i, j - 1)
        elif dp[i][j] == dp[i + 1][j - 1] + pair((seq[i], seq[j])):
            fold.append((i, j))
            traceback(dp, seq, fold, i + 1, j - 1)
        else:
            for k in range(i + 1, j - 1):
                if dp[i][j] == dp[i, k] + dp[k + 1][j]:
                    traceback(dp, seq, fold, i, k)
                    traceback(dp, seq, fold, k + 1, j)
                    break
    return fold


def nussinov(seq):
    dp = initialize(seq)
    n = len(seq)
    for k in range(1, n):
        for i in range(n - k):
            j = i + k
            if j - 1 >= minimum_loop_length:
                down = dp[i + 1][j]
                left = dp[i][j - 1]
                diag = dp[i + 1][j - 1] + pair((seq[i], seq[j]))

                rc = max([dp[i][t] + dp[t + 1][j] for t in range(i, j)])

                dp[i][j] = max(down, left, diag, rc)
            else:
                dp[i][j] = 0
    return dp


def initialize(seq):
    # initialize dp array for use in Nussinov algorithm
    n = len(seq)

    dp = np.empty([n, n])
    dp[:] = np.NAN
    dp[range(n), range(n)] = int(0)
    dp[range(1, n), range(n - 1)] = int(0)

    return dp


def main():
    seq = 'CUCGUCGCCUUAAUCCAGUGCGGGCGCUAGACAUCUAGUUAUCGCCGCAA'
    dp = nussinov(seq)
    fold = []
    sec = traceback(dp, seq, fold, 0, len(dp) - 1)
    res = dot_write(seq, fold)
    names = [_ for _ in seq]
    df = pd.DataFrame(dp, index=names, columns=names)
    # print(df, "\n", seq, res)
    print(seq, res)


main()
exit(0)

