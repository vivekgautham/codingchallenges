import unittest
from challenges.src.datastructures import graph
import functools

class Test_DiGraph(unittest.TestCase):

    def test_GraphDfs(self):
        g = graph.DiGraph()
        g.addEdge(0, 1) 
        g.addEdge(0, 2) 
        g.addEdge(1, 2) 
        g.addEdge(2, 0) 
        g.addEdge(2, 3) 
        g.addEdge(3, 3) 
        res = []

        def fn(res, n):
            res.append(n)

        fnt = functools.partial(fn, res)
        g.dfs(2, fnt)
        self.assertEqual(res, [2, 0, 1, 3])

        g1 = graph.DiGraph()
        g1.addEdge('0', '1') 
        g1.addEdge('0', '2') 
        g1.addEdge('1', '2') 
        g1.addEdge('2', '0') 
        g1.addEdge('2', '3') 
        g1.addEdge('3', '3') 
        res = []

        def fn1(res, n):
            res.append(n)

        fnt = functools.partial(fn1, res)
        g1.dfs('2', fnt)
        self.assertEqual(res, ['2', '0', '1', '3'])

    def test_GraphBfs(self):
        g = graph.DiGraph()
        g.addEdge(0, 1) 
        g.addEdge(0, 2) 
        g.addEdge(1, 2) 
        g.addEdge(2, 0) 
        g.addEdge(2, 3) 
        g.addEdge(3, 3) 
        res = []

        def fn(res, n):
            res.append(n)

        fnt = functools.partial(fn, res)
        g.bfs(2, fnt)
        self.assertEqual(res, [2, 0, 3, 1])

    def test_GraphCycle(self):
        g = graph.DiGraph()
        g.addEdge(0, 1)
        g.addEdge(1, 2) 
        g.addEdge(2, 0) 
        g.addEdge(3, 4) 
        g.addEdge(4, 5)
        self.assertEqual(g.isCycle(), True)
        
        g1 = graph.DiGraph()
        g1.addEdge(0, 1) 
        g1.addEdge(0, 2) 
        g1.addEdge(1, 3)
        g1.addEdge(2, 4)
        self.assertEqual(g1.isCycle(), False)
        


if __name__ == '__main__':
    unittest.main()