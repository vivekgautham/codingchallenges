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
