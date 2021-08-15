from collections import deque
from dataclasses import dataclass

class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def buildTree(inorder, preorder):

    def _buildTreeRecurse(inorder, preorder, instart, inend):
        if instart > inend:
            return None
        tmpNode = Node(preorder[_buildTreeRecurse.preOrderIndex])
        _buildTreeRecurse.preOrderIndex += 1
        if instart == inend:
            return tmpNode
        inIdx = None
        for i in range(instart, inend+1):
            if inorder[i] == tmpNode.value:
                inIdx = i
        tmpNode.left = _buildTreeRecurse(inorder, preorder, instart, inIdx-1)
        tmpNode.right = _buildTreeRecurse(inorder, preorder, inIdx+1, inend)
        return tmpNode

    _buildTreeRecurse.preOrderIndex = 0
    root = _buildTreeRecurse(inorder, preorder, 0, len(inorder)-1)
    return root

def inorder(root, arr):
    if root is None:
        return
    inorder(root.left, arr)
    arr.append(root.value)
    inorder(root.right, arr)

def inorderSuccessor(root, elem):
    arr = []
    inorder(root, arr)
    return arr[arr.index(elem)+1]

def levelOrderTraversal(root, lo=[]):

    if root is None: return lo

    q = deque()
    q.append(root)

    while q:
        s = q.popleft()

        lo.append(s.value)
        if s.left:
            q.append(s.left)
        if s.right:
            q.append(s.right)
    return lo

def getLevelDepth(root):

    levelDepthDict = {}
    if root is None: return levelDepthDict

    q = deque()
    q.append((root, 0))

    while q:
        s, d = q.popleft()

        levelDepthDict[s.value] = d
        if s.left:
            q.append((s.left, d+1))
        if s.right:
            q.append((s.right, d+1))
    return levelDepthDict


@dataclass
class FenwickTree():

    inputArray : list

    def __post_init__(self):
        self.sumArray = [0]*(len(self.inputArray)+1)
        for i, each in enumerate(self.inputArray):
            self.update(each, i, len(self.inputArray))

    def update(self, element, idx, n):
        idx = idx+1
        while idx <= n:
            self.sumArray[idx] += element
            idx += (idx & (-idx))

    def getRangeSum(self, en):
        s = 0
        idx = en+1
        while idx > 0:
            s += self.sumArray[idx]
            idx -= (idx & (-idx))
        return s


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.tree = collections.defaultdict(set)
        for i, e in enumerate(parent):
            self.tree[e].add(i)

    def getKthAncestor(self, node: int, k: int) -> int:
        ans = ['']
        def _dfs(nd, path):
            if node in self.tree[nd]:
                ans[0] = path
            else:
                for e in self.tree.get(nd, []):
                    newpath = path + '{e}->'.format(e=e)
                    #print(newpath)
                    _dfs(e, newpath)

        #print(self.tree)
        _dfs(-1, '-1->')
        #print(ans)
        l = ans[0].rstrip('->').split('->')[::-1]
        #print(l)
        return l[k-1]

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.childrenToParent = {}
        for i, e in enumerate(parent):
            self.childrenToParent[i] = e
        #print(self.childrenToParent)
        self.treeUpwards = {}
        for node in range(n):
            self.treeUpwards[node] = self._getToRoot(node)
        print(self.treeUpwards)
    def _getToRoot(self, node):
        if node == -1:
            return []
        elif node in self.treeUpwards:
            return self.treeUpwards[node]
        else:
            par = self.childrenToParent[node]
            return [par] + self._getToRoot(par)


    def getKthAncestor(self, node: int, k: int) -> int:
        return self.treeUpwards[node][k-1] if k < len(self.treeUpwards[node]) else -1







