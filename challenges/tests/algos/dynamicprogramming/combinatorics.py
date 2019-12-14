import unittest
from challenges.src.algos.dynamicprogramming import combinatorics

class Test_Combinatorics(unittest.TestCase):

    def test_CountWays(self):
        self.assertEqual(combinatorics.countWays(4, 2), 5)
        self.assertEqual(combinatorics.countWays(3, 3), 4)

    def test_allWays(self):
        self.assertEqual(combinatorics.allWays(4, 2), [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]])
        self.assertEqual(combinatorics.allWays(3, 3), [[1, 1, 1], [1, 2], [2, 1], [3]])

    def test_minCoinChange(self):
        self.assertEqual(combinatorics.minimumCoins(31, [25, 10, 1]), 4)
        self.assertEqual(combinatorics.minimumCoins(35, [25, 10, 1]), 2)
        self.assertEqual(combinatorics.minimumCoins(34, [25, 10, 1]), 7)

if __name__ == '__main__':
    unittest.main()