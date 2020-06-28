import sys
from random import randint

def isTwoElemSum(sum, array):
    diff = set()
    for each in array:
        if each in diff:
            return True
        else:
            diff.add(sum - each)
    return False

def productPuzzle(array):
    prodArray = [1]*len(array)
    temp = 1
    for i in range(0, len(array)):
        prodArray[i] = temp
        temp *= array[i]

    temp = 1
    for i in range(len(array), 0, -1):
        prodArray[i] *= temp
        temp *= array[i]

    return prodArray

def kadane(array):
    maxSoFar = -sys.maxsize - 1
    maxUntil = 0
    for e in array:
        maxUntil += e
        maxSoFar = max(maxUntil, maxSoFar)
        if maxUntil < 0:
            maxUntil = 0
    return maxSoFar

def maxRectangleArea(array):
    stack = list()
    i = 0
    maxArea = 0
    while (i < len(array)):
        if not stack or array[stack[-1]] <= array[i]:
            stack.append(i)
            i += 1
        else:
            curMax = stack.pop()
            area = array[curMax] * (i -1 - stack[-1] if stack else i)
            maxArea = max(maxArea, area)

    while (stack):
        curMax = stack.pop()
        area = array[curMax] * (i -1 - stack[-1] if stack else i)
        maxArea = max(maxArea, area)

    return maxArea

def cycleInArray(array):
    p = q = 0
    while True:
        if (p < 0 or q < 0 or p >= len(array) or q >= len(array)):
            return False
        p = array[p]
        if p == q: return True
        if (p < 0 or p >= len(array)):
            return False
        p = array[p]
        if p == q: return True
        q = array[q]
        if p == q: return True
    return False

def kthElementOfTwoSortedArray(array1, array2, k):
    ct = 0
    i = 0
    j = 0
    elem = None
    while (ct < k):
        if i < len(array1) and j < len(array2):
            if array1[i] <= array2[j]:
                elem = array1[i]
                i += 1
            else:
                elem = array2[j]
                j += 1
        elif i < len(array1):
            elem = array1[i]
            i += 1
        else:
            elem = array2[j]
            j += 1
        ct += 1
    return elem

def rgbSort(array):
    """ Inplace sorting of an array containing RGB value in order 'R', 'G', 'B' """
    low = 0
    middle = 0
    high = len(array) - 1
    while (middle <= high):
        if array[middle] == 'R':
            array[low], array[middle] = array[middle], array[low]
            low += 1
            middle += 1
        elif array[middle] == 'B':
            array[high], array[middle] = array[middle], array[high]
            high -= 1
        else:
            middle += 1
    return array

def detectNonDupsInNDupsArray(array):
    ones = 0
    twos = 0
    for e in array:
        twos = twos | (ones & e)
        ones = ones ^ e
        common = ~ (ones & twos)
        ones &= common
        twos &= common
    return ones

def singleSellProfit(array):
    if not len(array):
        return 0
    profit = 0
    cheapest = array[0]
    for e in array:
        cheapest = min(cheapest, e)
        profit = max(profit, e-cheapest)
    return profit

def findMissingOne(fullArray, arrayWithElementMissing):
    xorsum = 0
    for each in fullArray:
        xorsum ^= each
    for each in arrayWithElementMissing:
        xorsum ^= each
    return xorsum

def findMinOperationToSortedArray(array):

    sm = min(array)
    lg = max(array)

    minOps = [[sys.maxsize for k in range(lg+1)] for e in range(len(array))]
    for j in range(sm, lg+1):
        minOps[0][j] = abs(array[0]-j)

    for i in range(1, len(array)):
        minInRow = sys.maxsize
        for j in range(sm, lg+1):
            minInRow = min(minInRow, minOps[i-1][j])
            minOps[i][j] = minInRow + abs(array[i]-j)

    res = sys.maxsize

    for j in range(sm, lg+1):
        res = min(res, minOps[len(array)-1][j])

    return res

def hIndex(citations):
    left = 0
    right = len(citations)-1

    while (left <= right):
        mid = left + (right-left)//2
        if citations[mid] >= len(citations)-mid:
            right = mid-1
        else:
            left = mid+1
    return len(citations) - (right+1)

def sortedArrayMedian(arr):
    if len(arr) % 2 == 1:
        median = arr[len(arr)//2]
    else:
        median = 0.5*sum([arr[len(arr)//2-1], arr[len(arr)//2]])
    return median

def naiveMedian(arr):
    arr.sort()
    median = sortedArrayMedian(arr)
    return median

def median(arr):
    if len(arr) <= 5:
        return naiveMedian(arr)

    if len(arr) % 2 == 1:
        _quickSelectMedian(arr, 0, len(arr)-1, len(arr)//2)
    else:
        _quickSelectMedian(arr, 0, len(arr)-1, len(arr)//2)
        _quickSelectMedian(arr, 0, len(arr)-1, len(arr)//2-1)
    return sortedArrayMedian(arr)

def isSortedUpto(arr, k):
    return all([a <= b for a, b in zip(arr[:k+1], arr[1:k+1])])

def _getLastIndexOf(arr, pivot):
    resIdx = None
    for idx, each in enumerate(arr):
        if each == pivot:
            resIdx = idx
    return resIdx

def _quickSelectMedian(arr, l, r, comp):
    if r-l < 1:
        return
    pivotIdx = randint(l, r)
    pivot = arr[pivotIdx]
    partition(arr, l, r, pivotIdx)
    pivotIdxNew = _getLastIndexOf(arr, pivot)
    if pivotIdxNew > comp:
        return _quickSelectMedian(arr, l, pivotIdxNew-1, comp)
    else:
        return _quickSelectMedian(arr, pivotIdxNew+1, r, comp)

def partition(arr, lowIdx, highIdx, pivotIdx):
    pivot = arr[pivotIdx]
    arr[highIdx], arr[pivotIdx] = arr[pivotIdx], arr[highIdx]
    i = lowIdx-1
    for j in range(lowIdx, highIdx):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[highIdx] = arr[highIdx], arr[i+1]
    return arr

def maxSumWithoutAdjacentElements(arr):
    sumExcludingLatest = 0
    sumNotIncludingCurr = 0
    sumIncludingLatest = 0
    for curr in arr:
        sumNotIncludingCurr = max(sumExcludingLatest, sumIncludingLatest)
        sumIncludingLatest = sumExcludingLatest + curr
        sumExcludingLatest = sumNotIncludingCurr
    return max(sumNotIncludingCurr, sumIncludingLatest)


















