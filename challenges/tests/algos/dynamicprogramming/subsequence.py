import unittest
from challenges.src.algos.dynamicprogramming import subsequence

class Test_Subsequence(unittest.TestCase):

    def test_subsequence(self):
        self.assertEqual(subsequence.longestIncreasingSubsequenceLength([5, 8, 1, 2, 4, 7, 10, 24]), 6)
        self.assertEqual(subsequence.longestIncreasingSubsequenceLength([10, 22, 9, 33, 21, 50, 41, 60]), 5)
        self.assertEqual(subsequence.longestIncreasingSubsequenceLength([51, 7, 2, 94, 49, 30, 24, 85, 55, 57, 41]), 4)