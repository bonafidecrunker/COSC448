# returns the longest common subsequence between two input strings
def longest_common_subsequence(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for i in range(m + 1)]

    # build a matrix using dp to determine the longest common subsequence
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # generate the longest common subsequence using the dp matrix
    output = ''
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            output += text1[i - 1]
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(output))

def shortest_common_supersequence(str1, str2):
    output, i, j = '', 0, 0
    for c in longest_common_subsequence(str1, str2):
        while str1[i] != c:
            output += str1[i]
            i += 1
        while str2[j] != c:
            output += str2[j]
            j += 1
        output += c
        i += 1
        j += 1

    return output + str1[i:] + str2[j:]


