from collections import deque
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


     
