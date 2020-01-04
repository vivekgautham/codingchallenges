import unittest
from challenges.src.algos import arrays

class Test_Arrays(unittest.TestCase):

    def test_kadane(self):
        self.assertEqual(arrays.kadane([1, 2, -2, -4, 6, 7, -2]), 13)

    def test_maxAreaRectangleHistogram(self):
        self.assertEqual(arrays.maxRectangleArea([1, 2, 3, 4, 5, 3, 3, 2]), 15)
        self.assertEqual(arrays.maxRectangleArea([2, 1, 1, 3, 4, 1, 3, 2]), 8)
        self.assertEqual(arrays.maxRectangleArea([1, 3, 2, 5]), 6)

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

    def test_findMissingOne(self):
        self.assertEqual(arrays.findMissingOne([2], []), 2)
        self.assertEqual(arrays.findMissingOne([-2], []), -2)
        self.assertEqual(arrays.findMissingOne([0], []), 0)
        self.assertEqual(arrays.findMissingOne([4, 5, 6], [6, 4]), 5)
        self.assertEqual(arrays.findMissingOne([4, 5, 5, 6], [6, 5, 4]), 5)

    def test_findMinOperationToSortedArray(self):
        self.assertEqual(arrays.findMinOperationToSortedArray([1, 2, 1, 4, 3]), 2)
        self.assertEqual(arrays.findMinOperationToSortedArray([1, 2, 2, 4]), 0)
        self.assertEqual(arrays.findMinOperationToSortedArray([1, 5, 4, 2, 3]), 4)

    def test_hIndex(self):
        self.assertEqual(arrays.hIndex([2, 7, 9, 12, 14]), 4)
        self.assertEqual(arrays.hIndex([0, 0, 2, 3, 4]), 2)

    def test_naiveMedian(self):
        self.assertEqual(arrays.naiveMedian([4, 8, 2, 5, 3, 3]), 3.5)
        self.assertEqual(arrays.naiveMedian([4, 8, 2, 5, 3, 3, 7, 12]), 4.5)
        self.assertEqual(arrays.naiveMedian([9, 1, 0, 2, 3, 4, 6, 8, 7, 10, 5]), 5)
        self.assertEqual(arrays.naiveMedian([4, 2, 1, 3]), 2.5)

    def test_partition(self):
        self.assertEqual(arrays.partition([4, 8, 2, 5, 3, 3], 0, 5, 3), [4, 2, 3, 3, 5, 8])
        self.assertEqual(arrays.partition([4, 8, 2, 5, 3, 3], 0, 5, 0), [3, 2, 3, 4, 8, 5])
        self.assertEqual(arrays.partition([3, 1, 9, 8, 2, 1, 0, 3], 0, 7, 0), [3, 1, 2, 1, 0, 3, 9, 8])

    def test_median(self):
        self.assertEqual(arrays.median([22, 33, 0, 22, 3, 34, 2]), 22)
        self.assertEqual(arrays.median([4, 8, 2, 5, 3, 3]), 3.5)
        self.assertEqual(arrays.median([4, 8, 2, 5, 3, 3, 7, 12]), 4.5)
        self.assertEqual(arrays.median([2]), 2)
        self.assertEqual(arrays.median([2, 1]), 1.5)
        self.assertEqual(arrays.median([2, 1, 3]), 2)

        self.assertEqual(arrays.median([4, 2, 1, 3]), arrays.naiveMedian([4, 2, 1, 3]))
        self.assertEqual(arrays.median([9, 1, 0, 2, 3, 4, 6, 8, 7, 10, 5]), arrays.naiveMedian([9, 1, 0, 2, 3, 4, 6, 8, 7, 10, 5]))




if __name__ == '__main__':
    unittest.main()