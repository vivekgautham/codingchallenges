import unittest
from challenges.src.algos.geometry import points


class Test_Points(unittest.TestCase):

    def test_ClosestPoints(self):
        self.assertEqual(points.closestPoints([(0, 0), (5, 4), (3, 1)], (1, 2), 2), [(0, 0), (3, 1)])