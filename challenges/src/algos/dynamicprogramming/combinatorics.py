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
    if n == 0 or k == 0: return [[]]
    def _findWays(cur ,n, k, arr):
        if cur>n:
            return
        arr.append(cur)
        if cur == n:
            k = 0
            ll = []
            for e in arr:
                ll.append(e-k)
                k = e
            res.append(ll)
        for i in range(1, k+1):
            _findWays(cur+i, n, k, arr)
        arr.pop()

    arr = []
    for i in range(1, k+1):
        _findWays(i ,n, k, arr)
    return res

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