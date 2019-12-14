import unittest
from challenges.src.datastructures import trees

class Test_Trees(unittest.TestCase):

    def test_BuildTree(self):
        inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
        preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
        root = trees.buildTree(inOrder, preOrder)
        self.assertEqual(root.value, 'A')
        self.assertEqual(root.left.value, 'B')
        self.assertEqual(root.right.value, 'C')
        self.assertEqual(root.right.left.value, 'F')
        self.assertEqual(root.left.left.value, 'D')
        self.assertEqual(root.left.right.value, 'E')

    def test_LevelOrderTraversal(self):
        root = trees.Node(20)
        root.left = trees.Node(10)
        root.left.left = trees.Node(4)
        root.left.right = trees.Node(18)
        root.right = trees.Node(26)
        root.right.left = trees.Node(24)
        root.right.right = trees.Node(27)
        root.left.right.left = trees.Node(14)
        root.left.right.left.left = trees.Node(13)
        root.left.right.left.right = trees.Node(15)
        root.left.right.right = trees.Node(19)
        res = trees.levelOrderTraversal(root)
        self.assertEqual(res, [20, 10, 26, 4, 18, 24, 27, 14, 19, 13, 15])

if __name__ == '__main__':
    unittest.main()