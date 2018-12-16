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