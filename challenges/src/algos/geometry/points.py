import math

from challenges.src.datastructures.stack import MinHeap

def closestPoints(points, centralPoint, k):
    mH = MinHeap([])
    for point in points:
        mH.push((math.sqrt((centralPoint[0]-point[0])**2 + (centralPoint[1]-point[1])**2), point))
    result = []
    for i in range(k):
        result.append(mH.pop()[1])
    return result

