

def regularExpressionMatching(s, p):
    table = [[False]*(len(s)+1) for i in range(len(p)+1)]
    table[0][0] = True
    for k in range(1, len(p)+1):
        if p[k-1] == '*':
            table[k][0] = True

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            if p[i-1] == s[j-1] or p[i-1] == '.':
                table[i][j] = table[i-1][j-1]
            else:
                if p[i-1] == '*':
                    if table[i-2][j]:
                        table[i][j] = True
                    if table[i][j-1]:
                        if (s[j-1] == p[i-2] or p[i-2] == '.'):
                            table[i][j] = True

    return table[len(p)][len(s)]