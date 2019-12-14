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

