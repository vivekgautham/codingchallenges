import heapq
from dataclasses import dataclass

@dataclass
class MaxHeap(object):

    heaparray : list

    def push(self, item):
        heapq.heappush(self.heaparray, item)

    def pop(self):
        return heapq.heappop(self.heaparray)

@dataclass
class Stack(object):

    maxheap : MaxHeap = MaxHeap([]) 
    counter : int = 0

    def push(self, item):
        self.maxheap.push((self.counter, item))
        self.counter -= 1

    def pop(self):
        return self.maxheap.pop()[1]

    