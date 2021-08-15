import unittest
from challenges.src.algos.dynamicprogramming import combinatorics

class Test_Combinatorics(unittest.TestCase):

    def test_CountWays(self):
        self.assertEqual(combinatorics.countWays(4, 2), 5)
        self.assertEqual(combinatorics.countWays(3, 3), 4)

    def test_allWays(self):
        self.assertEqual(combinatorics.allWays(4, 2), [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]])
        self.assertEqual(combinatorics.allWays(3, 3), [[1, 1, 1], [1, 2], [2, 1], [3]])
        self.assertEqual(combinatorics.allWays(6, [1, 3]), [[1, 1, 1, 1, 1, 1], [1, 1, 1, 3], [1, 1, 3, 1], [1, 3, 1, 1], [3, 1, 1, 1], [3, 3]])
        self.assertEqual(combinatorics.allWays(6, [1, 3, 6]), [[1, 1, 1, 1, 1, 1], [1, 1, 1, 3], [1, 1, 3, 1], [1, 3, 1, 1], [3, 1, 1, 1], [3, 3], [6]])
        self.assertEqual(combinatorics.allWays(6, [1, 3, 6, 7]), [[1, 1, 1, 1, 1, 1], [1, 1, 1, 3], [1, 1, 3, 1], [1, 3, 1, 1], [3, 1, 1, 1], [3, 3], [6]])

    def test_minCoinChange(self):
        self.assertEqual(combinatorics.minimumCoins(31, [25, 10, 1]), 4)
        self.assertEqual(combinatorics.minimumCoins(35, [25, 10, 1]), 2)
        self.assertEqual(combinatorics.minimumCoins(34, [25, 10, 1]), 7)

    def test_CountWays(self):
        self.assertEqual(combinatorics.cutRod(8, {1: 1, 2:5}), 20)
        self.assertEqual(combinatorics.cutRod(8, {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20}), 22)
        self.assertEqual(combinatorics.cutRod(8, {1:3, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20}), 24)

    def test_isThereSubSetSum(self):
        self.assertEqual(combinatorics.isThereSubSetSum(4, {1, 5, 2}), False)
        self.assertEqual(combinatorics.isThereSubSetSum(9, {4, 1, 10, 12, 5, 2}), True)
        self.assertEqual(combinatorics.isThereSubSetSum(3, {1, 5, 2, 5}), True)

    def test_subSetDivideMinimalDifferenceSum(self):
        self.assertEqual(combinatorics.subSetDivideMinimalDifferenceSum([5, 10, 15, 20, 25]), ([5, 10, 20], [15, 25]))

if __name__ == '__main__':
    unittest.main()