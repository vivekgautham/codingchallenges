def findFirstSubstrIndex(s, x):
    i = 0
    j = 0
    while (i < len(s)):
        if (s[i] == x[j]):
            j += 1
            if j == len(x):
                return i - j + 1
        else:
            i -= j
            j = 0
        i += 1
    return -1

def levenshteinDistance(s, t):
    if len(s) < len(t):
        return levenshteinDistance(t, s)
    mat = []
    for i in range(len(t)+1):
        if i == 0:
            mat.append(list(range(len(s)+1)))
        else:
            mat.append([i] + [0]*len(s))
    for i1, e1 in enumerate(t):
        for i2, e2 in enumerate(s):
            if e1 == e2:
                mat[i1+1][i2+1] = mat[i1][i2]
            else:
                mat[i1+1][i2+1] = 1+min([mat[i1][i2], mat[i1+1][i2], mat[i1][i2+1]])
    return mat[-1][-1]

def longestPalindromeSubstr(s):
    n = len(s)
    t = [[False]*n for i in range(0, n)]
    for i in range(n):
        t[i][i] = True
    start = 0
    mL = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            t[i][i+1] = True
            start = i
            mL = 2

    for i in range(2, n):
        for j in range(0, n-i):
            k = i + j
            if t[j+1][k-1] and s[j] == s[k]:
                t[j][k] = True
                if i+1 > mL:
                    mL = i+1
                    start = j

    return s[start:start+mL]