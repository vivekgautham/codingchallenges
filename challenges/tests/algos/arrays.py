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

    def test_RGBSort(self):
        self.assertEqual(arrays.rgbSort(['G', 'B', 'R', 'R', 'B', 'R', 'G']), ['R', 'R', 'R', 'G', 'G', 'B', 'B'])
        self.assertEqual(arrays.rgbSort(['B', 'G', 'R']), ['R', 'G', 'B'])
        self.assertEqual(arrays.rgbSort(['B', 'G', 'B', 'R', 'G']), ['R', 'G', 'G', 'B', 'B'])
        self.assertEqual(arrays.rgbSort(['R', 'B', 'G', 'B', 'R']), ['R', 'R', 'G', 'B', 'B'])

    def test_NonDups(self):
        self.assertEqual(arrays.detectNonDupsInNDupsArray([6,1,3,3,3,6,6]), 1)
        self.assertEqual(arrays.detectNonDupsInNDupsArray([13, 19, 13, 13]), 19)
        self.assertEqual(arrays.detectNonDupsInNDupsArray([3,3,3]), 0)
        self.assertEqual(arrays.detectNonDupsInNDupsArray([3,3,3,2]), 2)
        self.assertEqual(arrays.detectNonDupsInNDupsArray([3,3,2,2,2]), 0)

    def test_singleSellProfit(self):
        self.assertEqual(arrays.singleSellProfit([9, 11, 8, 5, 7, 10]), 5)
        self.assertEqual(arrays.singleSellProfit([3, 3, 3, 3]), 0)
        self.assertEqual(arrays.singleSellProfit([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), 0)
        self.assertEqual(arrays.singleSellProfit([2, 7, 1, 8, 2, 8, 4, 5, 9, 0, 4, 5]), 8)

if __name__ == '__main__':
    unittest.main()