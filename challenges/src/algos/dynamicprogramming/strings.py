
import collections

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

def spellchecker(wordlist, queries):
        vow = {'a', 'e', 'i', 'o', 'u'}
        def mask(e):
            return ''.join(['*' if ch in vow else ch for ch in e])

        result = []
        wls = set()
        lowDict = collections.defaultdict(list)
        maskDict = collections.defaultdict(list)
        for e in wordlist:
            wls.add(e)
            lowDict[e.lower()].append(e)
            maskDict[mask(e.lower())].append(e)

        for each in queries:
            if each in wls:
                result.append(each)
            elif each.lower() in lowDict:
                result.append(lowDict[each.lower()][0])
            elif mask(each.lower()) in maskDict:
                result.append(maskDict[mask(each.lower())][0])
            else:
                result.append("")

        return result