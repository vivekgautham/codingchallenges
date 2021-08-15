
import unittest
from challenges.src.datastructures import heap

class Test_Heap(unittest.TestCase):

    def test_heapWays(self):
        self.assertEqual(heap.solve(5), 8)
        self.assertEqual(heap.solve(7), 80)
        self.assertEqual(heap.solve(10), 3360)