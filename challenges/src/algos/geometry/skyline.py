import heapq

def getSkyLine(buildings):
    result = []
    bc = []
    class Point(object):
        
        def __init__(self, x, y, se):
            self.x = x
            self.y = y
            self.se = se
            
        def __lt__(self, other):
            if self.x < other.x: return True
            if self.x > other.x: return False
            if self.x == other.x:
                if (self.se == 's' and other.se == 's') or (self.se == 'e' and other.se == 's') or (self.se == 's' and other.se == 'e'):
                    if self.y > other.y: return True
                    if self.y < other.y: return False
                else:
                    if self.y < other.y: return True
                    if self.y > other.y: return False
                
            return False
        
        def __eq__(self, other):
            return self.x == other.x and self.y == other.y and self.se == other.se
        
            
    for e in buildings:
        bc.append(Point(e[0], e[2], 's'))
        bc.append(Point(e[0]+e[1], e[2], 'e'))
    bc.sort()
    l = [0]
    curMin = 0
    for e in bc:
        if e.se == 's':
            negH = -e.y
            heapq.heappush(l, negH)
            if negH < curMin:
                curMin = negH
                if result and result[-1] == [e.x, 0]: result.pop()
                result.append([e.x, e.y])
        if e.se == 'e':
            i = l.index(-e.y)
            l[i], l[-1] = l[-1], l[i]
            l.pop()
            if i < len(l):
                heapq._siftup(l, i)
                heapq._siftdown(l, 0, i)
                
            m = min(l)
            if curMin != m:
                curMin = m
                if result and result[-1] == [e.x, 0]: result.pop()
                result.append([e.x, -m])
    return result

