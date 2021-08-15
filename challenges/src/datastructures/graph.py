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


def isFlower(adj):
    ''' Check if adjacency matrix has flower format'''
    connections = defaultdict(set)
    maxOrderNode = None
    maxOrder = 0
    for i in range(len(adj)):
        for j in range(len(adj[0])):
            if i == j:
                if adj[i][j]:
                    return False
            if adj[i][j]:
                connections[i].add(j)
                if len(connections[i]) > maxOrder:
                    maxOrder = len(connections[i])
                    maxOrderNode = i

    def _dfs(e, visited, group, newconnections):
        group.add(e)
        visited[e] = True
        for node in newconnections.get(e, []):
            if not visited[node]:
                _dfs(node, visited, group, newconnections)

    if maxOrderNode is not None:
        newAdj = [row[:maxOrderNode] + row[maxOrderNode+1:] for idx, row in enumerate(adj) if idx != maxOrderNode]
        newconnections = defaultdict(set)
        for i in range(len(newAdj)):
            for j in range(len(newAdj[0])):
                if newAdj[i][j]:
                    newconnections[i].add(j)

        groupLengths = set()
        edgesLengths = set()
        visited = [False]*len(newAdj)
        complete = True
        for e in range(len(newAdj)):
            group = set()
            if not visited[e]:
                _dfs(e, visited, group, newconnections)
                if group:
                    groupLengths.add(len(group))
                    edges = 0
                    for g in group:
                        edges += len(newconnections[g])
                    if edges != len(group)*(len(group)-1):
                        complete = False
                    edgesLengths.add(edges)

        return complete and (len(groupLengths) == 1) and (len(edgesLengths) == 1) and all(visited)
    return False


def isWheel(adj):
    ''' check if adjacency matrix has wheel format '''
    connections = defaultdict(list)
    for i, row in enumerate(adj):
        for j, val in enumerate(row):
            if val:
                connections[i].append(j)

    isCenter = False
    isSelf = False
    ctThree = 0
    for k, v in connections.items():
        if len(v) == len(adj)-1:
            isCenter = True
        if k in v:
            isSelf = True
        if len(v) == 3:
            ctThree += 1
    return ((ctThree == len(adj)-1) or (len(adj)-1) == 3 and ctThree == len(adj)) and not isSelf and isCenter



def isPseudoforest(n, wmap):
    from collections import defaultdict, deque
    graphDict = defaultdict(list)
    edgeCt = defaultdict(int)
    for each in wmap:
        graphDict[each[0]].append(each[1])
        edgeCt[each[0]] += 1

    if not graphDict:
        return True

    def _dfs(node, group, graphDict):
        if visited[node]:
            return
        group.add(node)
        visited[node] = True
        for eachNode in graphDict[node]:
            if not visited[eachNode]:
                _dfs(eachNode, group, graphDict)

    result = []
    visited = [False]*n
    for en in range(n):
        gp = set()
        _dfs(en, gp, graphDict)
        if len(gp) > 2:
            noe = 0
            for each in gp:
                noe += edgeCt.get(each, 0)
            result.append(noe - len(gp) + 1)
    return all([res <= 1 for res in result])


