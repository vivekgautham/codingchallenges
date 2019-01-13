from collections import defaultdict, deque

class DiGraph(object):

    def __init__(self):
        self.adjList = defaultdict(list)

    def addEdge(self, src, dst):
        self.adjList[src].append(dst)

    def bfs(self, start, fn):
        visited = {node:False for node in self.adjList.keys()}
        q = deque()
        q.append(start)
        visited[start] = True
        while q:
            c = q.popleft()
            fn(c) # function to do something with this node
            for e in self.adjList[c]:
                if not visited[e]:
                    q.append(e)
                    visited[e] = True
        return

    def _dfsRecurse(self, start, visited, fn):
        visited[start] = True
        fn(start) # function to do something with this node
        for e in self.adjList[start]:
            if not visited[e]:
                self._dfsRecurse(e, visited, fn)    

    def dfs(self, start, fn):
        visited = {node:False for node in self.adjList.keys()}
        self._dfsRecurse(start, visited, fn)

    def isCycle(self):
        inDegree = defaultdict(int)
        for e in self.adjList.keys():
            for e1 in self.adjList[e]:
                inDegree[e1] += 1
        q = deque()
        for e in self.adjList.keys():
            if inDegree[e] == 0:
                q.append(e)
        ct = 0
        while q:
            e = q.popleft()
            for p in self.adjList[e]:
                inDegree[p] -= 1
                if not inDegree[p]:
                    q.append(p)
            ct += 1
        if ct != len(self.adjList):
            return True
        return False



        

        
            




