import unittest
from challenges.src.algos import arrays

class Test_Arrays(unittest.TestCase):
    def test_kadane(self):
        self.assertEqual(arrays.kadane([1, 2, -2, -4, 6, 7, -2]), 13)

    def test_maxAreaRectangleHistogram(self):
        self.assertEqual(arrays.maxRectangleArea([1, 2, 3, 4, 5, 3, 3, 2]), 15)
        self.assertEqual(arrays.maxRectangleArea([2, 1, 1, 3, 4, 1, 3, 2]), 8)

    def test_cycleInArray(self):
        self.assertEqual(arrays.cycleInArray([1, 2, 1, 8, 3, 5]), True)
        self.assertEqual(arrays.cycleInArray([1, 2, 3, 4, 5, 6,]), False)

    def test_KthElementOfTwoSortedArray(self):
        self.assertEqual(arrays.kthElementOfTwoSortedArray([4, 34, 67, 400], [1, 2, 5], 3), 4)
        self.assertEqual(arrays.kthElementOfTwoSortedArray([4, 34, 67, 400], [1, 2, 5], 1), 1)
        self.assertEqual(arrays.kthElementOfTwoSortedArray([4, 5, 6, 7], [1, 2, 3], 5), 5)
        self.assertEqual(arrays.kthElementOfTwoSortedArray([1, 2, 3], [4, 5, 6, 7], 5), 5)

if __name__ == '__main__':
    unittest.main()