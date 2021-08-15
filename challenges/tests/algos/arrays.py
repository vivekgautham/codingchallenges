import unittest
from challenges.src.algos import arrays

class Test_Arrays(unittest.TestCase):

    def test_kadane(self):
        self.assertEqual(arrays.kadane([1, 2, -2, -4, 6, 7, -2]), 13)
        self.assertEqual(arrays.kadane([34, -50, 42, 14, -5, 86]), 137)
        self.assertEqual(arrays.kadane([-5, -1, -8, -9]), -1)

    def test_maxAreaRectangleHistogram(self):
        self.assertEqual(arrays.maxRectangleArea([1, 2, 3, 4, 5, 3, 3, 2]), 15)
        self.assertEqual(arrays.maxRectangleArea([2, 1, 1, 3, 4, 1, 3, 2]), 8)
        self.assertEqual(arrays.maxRectangleArea([1, 3, 2, 5]), 6)
        self.assertEqual(arrays.maxRectangleArea([2, 4, 5, 6, 3]), 12)
        self.assertEqual(arrays.maxRectangleArea([1,8,6,2,5,4,8,3,7]), 16)


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
        self.assertEqual(arrays.rgbSort(['G', 'B', 'R']), ['R', 'G', 'B'])

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

    def test_findInversion(self):
        self.assertEqual(arrays.findInversions([8, 4, 2, 1]), 6)
        self.assertEqual(arrays.findInversions([1, 20, 6, 4, 5]), 5)
        self.assertEqual(arrays.findInversions([1, 0, 2]), 1)


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

    def test_sortedArrayElementIndex(self):
        self.assertEqual(arrays.sortedArrayElementIndex([13, 18, 25, 2, 8, 10], 10), 5)
        self.assertEqual(arrays.sortedArrayElementIndex([13], 13), 0)
        self.assertEqual(arrays.sortedArrayElementIndex([13, 18], 18), 1)
        self.assertEqual(arrays.sortedArrayElementIndex([2, 3, 1], 3), 1)
        self.assertEqual(arrays.sortedArrayElementIndex([2, 3, 1], 1), 2)
        self.assertEqual(arrays.sortedArrayElementIndex([2, 3, 1], 2), 0)

    def test_maxSumWithoutAdjacentElements(self):
        self.assertEqual(arrays.maxSumWithoutAdjacentElements([6, 13, 97, 100, 7]), 113)
        self.assertEqual(arrays.maxSumWithoutAdjacentElements([1234]), 1234)
        self.assertEqual(arrays.maxSumWithoutAdjacentElements([7615, 2060, 7659, 6763, 6005, 6243, 2982, 5528, 2945]), 27206)
        self.assertEqual(arrays.maxSumWithoutAdjacentElements([5, 5, 5, 5, 5]), 15)
        self.assertEqual(arrays.maxSumWithoutAdjacentElements([1, 1111, 2, 3, 4444]), 5555)

    def test_smallestNumberNotInSubSetSum(self):
        self.assertEqual(arrays.smallestNumberNotInSubSetSum([1, 2, 3, 10]), 7)
        self.assertEqual(arrays.smallestNumberNotInSubSetSum([3, 4, 5]), 1)
        self.assertEqual(arrays.smallestNumberNotInSubSetSum([1, 2, 3, 4, 5]), 16)

    def test_stockSpan(self):
        self.assertEqual(arrays.stockSpan([7, 8, 6, 45, 3, 7]), [1, 2, 1, 4, 1, 2])
        self.assertEqual(arrays.stockSpan([17, 8, 16, 45, 13, 77]), [1, 1, 2, 4, 1, 6])
        self.assertEqual(arrays.stockSpan([10, 4, 5, 90, 120, 80]), [1, 1, 2, 4, 5, 1])
        self.assertEqual(arrays.stockSpan([100, 80, 60, 70, 60, 75, 85]), [1, 1, 1, 2, 1, 4, 6])


    def test_maxOccupancyTimeInterval(self):
        self.assertEqual(
            arrays.maxOccupancyTimeInterval([
                {"timestamp": 1, "count": 10, "type": "enter"},
                {"timestamp": 3, "count": 2, "type": "exit"},
                {"timestamp": 5, "count": 1, "type": "enter"},
                {"timestamp": 6, "count": 1, "type": "enter"},
                {"timestamp": 7, "count": 1, "type": "enter"},
                {"timestamp": 9, "count": 3, "type": "exit"},
                {"timestamp": 10, "count": 8, "type": "exit"}
            ]),
            (1, 7)
        )
        self.assertEqual(
            arrays.maxOccupancyTimeInterval([
                {"timestamp": 1, "count": 3, "type": "enter"},
                {"timestamp": 3, "count": 2, "type": "enter"},
                {"timestamp": 5, "count": 1, "type": "exit"},
                {"timestamp": 6, "count": 4, "type": "exit"},
            ]),
            (1, 3)
        )
        self.assertEqual(
            arrays.maxOccupancyTimeInterval([
                {"timestamp": 2, "count": 1, "type": "exit"},
                {"timestamp": 1, "count": 1, "type": "enter"},
                {"timestamp": 3, "count": 2, "type": "enter"},
                {"timestamp": 4, "count": 2, "type": "enter"},
                {"timestamp": 5, "count": 3, "type": "exit"},
                {"timestamp": 6, "count": 1, "type": "exit"},
            ]),
            (3, 4)
        )


if __name__ == '__main__':
    unittest.main()