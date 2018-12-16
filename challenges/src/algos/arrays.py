import sys

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
        if maxUntil > maxSoFar:
            maxSoFar = maxUntil
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



        

















