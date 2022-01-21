def kmp_algorithm(w, s):
    j = 0
    k = 0
    t = table_function(w)
    p = []

    while j < len(s):
        if w[k] == s[j]:
            j += 1
            k += 1
            if k == len(w):
                p.append(j - k)
                k = t[k - 1]
        else:
            k = t[k]
            if k < 0:
                j += 1
                k += 1
    return p


def table_function(string):
    t = [0] * len(string)
    pos = 1
    cnd = 0

    t[0] = -1

    while pos < len(string):
        if string[pos] == string[cnd]:
            t[pos] = t[cnd]
        else:
            t[pos] = cnd
            while cnd >= 0 and string[pos] != string[cnd]:
                cnd = t[cnd]
        pos += 1
        cnd += 1
    return t
