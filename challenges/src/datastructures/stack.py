import heapq
from dataclasses import dataclass

@dataclass
class MinHeap(object):

    heaparray : list

    def push(self, item):
        heapq.heappush(self.heaparray, item)

    def pop(self):
        return heapq.heappop(self.heaparray)

@dataclass
class Stack(object):

    minheap : MinHeap = MinHeap([])
    counter : int = 0

    def push(self, item):
        self.minheap.push((self.counter, item))
        self.counter -= 1

    def pop(self):
        return self.minheap.pop()[1]


class FreqStack:

    def __init__(self):
        from collections import defaultdict
        self.freqMap = defaultdict(int)
        self.setMap = defaultdict(list)
        self.maxFreq = 0

    def push(self, x: int) -> None:
        if x in self.freqMap:
            self.freqMap[x] += 1
            self.setMap[self.freqMap[x]].append(x)
            self.maxFreq = max(self.freqMap[x], self.maxFreq)
        else:
            self.freqMap[x] = 1
            self.setMap[1].append(x)
            self.maxFreq = max(self.maxFreq, 1)

        return

    def pop(self) -> int:
        elem = self.setMap[self.maxFreq].pop()
        self.freqMap[elem] -= 1
        if not self.setMap[self.maxFreq]:
            self.setMap.pop(self.maxFreq)
            self.maxFreq -= 1

        return elem