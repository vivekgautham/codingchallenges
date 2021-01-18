import itertools

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

def longestPalindromeSubstrAlternative(s):
    pal = ['']

    def _updatePal(low, high):
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if len(pal[0]) < len(s[low:high+1]):
                pal[0] = s[low:high+1]
            low -= 1
            high += 1

    for i in range(1, len(s)):
        high = i+1
        low = i-1
        _updatePal(low, high)
        high = i
        _updatePal(low, high)

    return pal[0]



def isPalindromeProducibleNaive(string, k):
    ''' Is Palindrome Producible by deleting atmost k characters '''
    if string == string[::-1]:
        return True
    idxs = list(range(len(string)))
    for each in range(1, k+1):
        for delIdxs in itertools.combinations(idxs, each):
            newSt = ''
            for idx, c in enumerate(string):
                if idx not in delIdxs:
                    newSt += c
            if newSt == newSt[::-1]:
                return True

    return False

def _getLastIndexOf(string, char):
    resIdx = None
    for idx, each in enumerate(string):
        if each == char:
            resIdx = idx
    return resIdx

def smallestWindowContainingAllDistinctChars(word):
    charSet = set(word)
    minWS = len(word)
    for i in range(len(word)):
        ws = 0
        windowCharSet = set()
        for ch in word[i:]:
            windowCharSet.add(ch)
            ws += 1
            if windowCharSet == charSet and ws < minWS:
                minWS = ws
                break
    return minWS

def smallestWindowContainingAllDistinctCharsOptimized(word):
    minWS = len(word)
    charCount = [0]*256
    start = 0
    distinctCount = len(set(word))
    count = 0
    startIdx = None
    for i in range(len(word)):
        charCount[ord(word[i])] += 1
        if charCount[ord(word[i])] == 1:
            count += 1
        if (count == distinctCount):
            while (charCount[ord(word[start])] > 1):
                charCount[ord(word[start])] -= 1
                start += 1

            currMinWS = i - start + 1
            if currMinWS < minWS:
                minWS = currMinWS
                startIdx = start
    return minWS

def largestSubStrContainingAtmostKDistinctChars(word, k):
    charCount = [0]*256
    start = 0
    maxWS = 0
    currentDistinctcount = 0
    startIdx = None
    for i in range(len(word)):
        charCount[ord(word[i])] += 1
        if charCount[ord(word[i])] == 1:
            currentDistinctcount += 1

        while (currentDistinctcount > k and charCount[ord(word[start])] > 0):
            charCount[ord(word[start])] -= 1
            if charCount[ord(word[start])] == 0:
                currentDistinctcount -= 1
            start += 1

        currMaxWS = i - start + 1
        if currMaxWS > maxWS:
            maxWS = currMaxWS
            startIdx = start

    return word[startIdx:startIdx+maxWS]


def isPalindromeProducible(string, k):

    def _isPalindromeProducibleRecurse(remainingString, delRemaining):
        if remainingString == remainingString[::-1]:
            return True
        if len(remainingString) <= delRemaining:
            return True
        if delRemaining <= 0:
            return False
        stChar = remainingString[0]
        stCharLastIdx = _getLastIndexOf(remainingString, stChar)
        delFirst = _isPalindromeProducibleRecurse(remainingString[1:], delRemaining-1)
        if stCharLastIdx in [0, None]:
            return delFirst
        else:
            delRemaining -= (len(remainingString) - (stCharLastIdx + 1))
            if delRemaining < 0:
                return False
            return delFirst or _isPalindromeProducibleRecurse(remainingString[1:stCharLastIdx], delRemaining)

    def _lcsLength(string):
        revString = string[::-1]
        l = [[0 for _ in range(0, len(string)+1)] for _ in range(0, len(string)+1)]
        for i in range(0, len(string)+1):
            for j in range(0, len(string)+1):
                if i == 0 or j == 0:
                    l[i][j] = 0
                elif string[i-1] == revString[j-1]:
                    l[i][j] = l[i-1][j-1] + 1
                else:
                    l[i][j] = max(l[i-1][j], l[i][j-1])
        return l[len(string)][len(string)]

    l = len(string)-_lcsLength(string)
    lcsStatus = l <= k
    recStatus = _isPalindromeProducibleRecurse(string, k)
    return lcsStatus and recStatus

def reverseWordsBetweenDelimiters(string, delimiters):
    stringStack = []
    delimiterStack = []
    startsWithDelimiters = string[0] in delimiters if string else False
    i = 0
    delimList = []
    curSt = ''

    while i < len(string):
        if string[i] in delimiters:
            if curSt:
                stringStack.append(curSt)
                curSt = ''
            delimList.append(string[i])
        else:
            if delimList:
                delimiterStack.append(delimList)
                delimList = []
            curSt += string[i]

        i += 1
    if curSt:
        stringStack.append(curSt)
    if delimList:
        delimiterStack.append(delimList)

    resStr = ''
    i = 0
    if startsWithDelimiters:
        resStr += ''.join(delimiterStack[i])
        i += 1
    while stringStack and i < len(delimiterStack):
        resStr += stringStack.pop()
        resStr += ''.join(delimiterStack[i])
        i += 1
    if i < len(delimiterStack):
        resStr += ''.join(delimiterStack[i])
        i += 1
    if stringStack:
        resStr += stringStack.pop()
    return resStr


def ladderLength(self, beginWord, endWord, wordList):
    from collections import defaultdict, deque
    connections = defaultdict(set)
    allWords = list(set(([beginWord] + wordList)))
    for i in range(len(allWords)):
        for j in range(i+1, len(allWords)):
            if sum([1 if ch1 != ch2 else 0 for ch1, ch2 in zip(allWords[i], allWords[j])]) == 1:
                connections[allWords[i]].add(allWords[j])
                connections[allWords[j]].add(allWords[i])

    visitedDict = {w:False for w in allWords}
    q = deque([(beginWord, 1)])
    visitedDict[beginWord] = True
    level = 0
    while q:
        wo, l = q.popleft()

        for each in connections.get(wo, []):
            if not visitedDict[each]:
                q.append((each, l+1))
                visitedDict[each] = True
                if each == endWord:
                    level = l+1
                    break
        if level:
            break

    return level






















