import unittest
from challenges.src.datastructures import graph_dfs
import functools

class Test_DFSUtils(unittest.TestCase):

    def test_GraphDfs(self):
        adj = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]
        ]
        self.assertEqual(graph_dfs.countIslands(adj), 5)

        adj = [
            [1, 1],
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(graph_dfs.countIslands(adj), 1)

if __name__ == '__main__':
    unittest.main()