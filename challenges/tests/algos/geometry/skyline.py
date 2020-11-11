

import unittest
from challenges.src.algos.geometry import skyline

class Test_Skyline(unittest.TestCase):

    def test_getSkyLine(self):
        res = skyline.getSkyLine([
            (1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16), (14, 3, 25),
            (19, 18, 22), (23, 26, 29), (24, 25, 28)]
        )
        self.assertEqual(res,
            [[1, 5], [2, 7], [3, 9], [12, 16], [14, 25], [17, 16], [19, 22], [23, 29], [49, 0]]

        )