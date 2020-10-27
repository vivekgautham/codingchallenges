from dataclasses import dataclass
from collections import deque
import heapq

@dataclass
class MinHeap(object):

    heaparray : list

    def push(self, item):
        heapq.heappush(self.heaparray, item)

    def pop(self):
        return heapq.heappop(self.heaparray)

class TypeAheadTrieLeaf:

    def __init__(self, identifier, score, counter):
        self.identifier = identifier
        self.score = score
        self.counter = counter

    def getHeapItem(self):
        return (-self.score, -self.counter)


class TypeAheadTrieNode:

    def __init__(self, elem):
        self.elem = elem
        self.children = []
        self.end = []

    def __eq__(self, other):
        return other.elem == self.elem

    def __str__(self):
        return '{0} - {1}'.format(self.elem, list(self.children))

    def __repr__(self):
        return '{0} - {1}'.format(self.elem, list(self.children))

class TypeAheadTrieTree:

    def __init__(self):
        self.root = TypeAheadTrieNode('*')
        self.counter = 1

    def display(self):
        dq = deque([self.root])
        while dq:
            cur = dq.popleft()
            al = ''
            for p in cur.children:
                al += '{0} '.format(p.elem)
                dq.append(p)
            print(al)

    def delete(self, identifier):
        dq = deque([self.root])
        while dq:
            cur = dq.popleft()
            delidxs = []
            for idx, e in enumerate(cur.end):
                if e.identifier == identifier:
                    delidxs.append(idx)
            ct = 0
            for idx in delidxs:
                cur.end.pop(idx-ct)
                ct += 1
            for p in cur.children:
                dq.append(p)

    def add(self, typ, identifier, score, dataString):
        for eachToken in dataString.split(" "):
            if eachToken:
                string = eachToken.lower()
                curNode = self.root
                for i, ch in enumerate(string):
                    # create node
                    node = TypeAheadTrieNode(ch)
                    # check if it exists in children
                    found = False
                    if curNode.children:
                        for child in curNode.children:
                            if child == node:
                                curNode = child
                                found = True
                    if not found:
                        curNode.children.append(node)
                        curNode = node
                curNode.end.append(TypeAheadTrieLeaf(identifier, float(score), self.counter))

        self.counter += 1

    def query(self, dataString):
        results = set()
        for string in dataString.split(" "):
            string = string.lower()
            if string:
                resultSet = set()
                curNode = self.root
                for i, ch in enumerate(string):
                    node = TypeAheadTrieNode(ch)
                    found = False
                    for each in curNode.end:
                        resultSet.add((each.getHeapItem(), each.identifier))

                    if curNode.children:
                        for child in curNode.children:
                            if child == node:
                                curNode = child
                                found = True

                    if not found:
                        return []

                if not resultSet:
                    # Visit each node underneath curNode and add ends if any
                    dq = deque([curNode])
                    while dq:
                        cur = dq.popleft()
                        for e in cur.end:
                            resultSet.add((e.getHeapItem(), e.identifier))
                        for p in cur.children:
                            dq.append(p)
                if not results:
                    results |= resultSet
                else:
                    results &= resultSet
        return list(results)

def typeaheadSearch(queries):
    tt = TypeAheadTrieTree()
    ct = 0
    allResults = []
    for each in queries:
        if each[0] == "ADD":
            tt.add(*each[1:])
        if each[0] == "QUERY":
            result = tt.query(each[2])
            mh = MinHeap([])
            idseen = set()
            for res in result:
                if res[1] not in idseen:
                    mh.push(res)
                    idseen.add(res[1])
            finalRes = []
            while mh.heaparray:
                ap = mh.pop()
                finalRes.append(ap[1])
            finalRes = finalRes[:int(each[1])]
            allResults.append(finalRes)
        if each[0] == "DEL":
            tt.delete(each[1])
    return allResults

