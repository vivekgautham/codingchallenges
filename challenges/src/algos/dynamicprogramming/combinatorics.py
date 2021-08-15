import collections
import sys

def countWays(n, k):
    if isinstance(k, collections.Iterable):
        karray = k
    else:
        karray = range(1, k+1)
    cache = [0]*(n+1)
    cache[0] = 1
    for i in range(0, n+1):
        cache[i] += sum([cache[i-x] for x in karray if i-x > 0])
        cache[i] += 1 if i in karray else 0
    return cache[-1]



def allWays(n, k):
    res = []
    if isinstance(k, collections.Iterable):
        karray = k
    else:
        karray = range(1, k+1)

    if n == 0 or len(karray) == 0: return [[]]

    def _findWays(cur, n, arr):
        if cur>n:
            return
        arr.append(cur)
        if cur == n:
            previous = 0
            outcome = []
            for e in arr:
                outcome.append(e-previous)
                previous = e
            res.append(outcome)
        for i in karray:
            _findWays(cur+i, n, arr)
        arr.pop()

    arr = []
    for i in karray:
        _findWays(i, n, arr)
    return res

def allDistinctWays(n, karray):
    res = []
    if n == 0 or len(karray) == 0: return [[]]

    def _findDistinctWays(idx, remaining, l):
        if remaining < karray[idx]:
            return
        else:
            l.append(karray[idx])
            remaining -= karray[idx]
            if remaining == 0:
                res.append([e for e in l])
            else:
                for i in range(idx+1, len(karray)):
                    _findDistinctWays(i, remaining, l)
        l.pop()

    for idx, e in enumerate(karray):
        l = []
        _findDistinctWays(idx, n, l)
    return res

def subSetDivideMinimalDifferenceSum(arr):
    halfSum = sum(arr)//2
    l = 1
    h = halfSum
    ways = None
    while halfSum:
        ways = allDistinctWays(halfSum, arr)
        if ways:
            break
        halfSum -= 1
    s1 = ways[0]
    s2 = [e for e in arr if e not in s1]
    return s1, s2


def minimumCoins(total, denominations):
    minCoins = [sys.maxsize]*(total+1)
    denominations = sorted(denominations)
    minCoins[0] = 0
    for i in range(1, total+1):
        for denom in denominations:
            if denom > i:
                break
            minCoins[i] = min(minCoins[i-denom]+1, minCoins[i])
    return minCoins[total]

def cutRod(size, priceDict):
    maxVals = []
    distinctLengths = sorted(priceDict.keys())
    for i in range(len(distinctLengths)):
        allVals = []
        for each in allWays(size, distinctLengths[:i+1]):
            allVals.append(sum([priceDict[r] for r in each]))
        maxVals.append(max(allVals))
    return max(maxVals)

def isThereSubSetSum(sum, subSet):
    if not sum or sum in subSet: return True
    cache = [[False for i in range(sum+1)] for j in range(len(subSet)+1)]
    for e in cache:
        e[0] = True
    arr = list(subSet)
    for i in range(1, len(subSet)+1):
        for j in range(1, sum+1):
            if j < arr[i-1]:
                cache[i][j] = cache[i-1][j]
            else:
                cache[i][j] = cache[i-1][j] or cache[i-1][j-arr[i-1]]

    return cache[len(subSet)][sum]



