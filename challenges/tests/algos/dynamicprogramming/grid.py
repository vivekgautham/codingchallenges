import unittest
from challenges.src.algos.dynamicprogramming import grid

class Test_Grid(unittest.TestCase):

    def test_mineLeftToRightUpDown(self):
        self.assertEqual(grid.mineLeftToRightUpDown(
            [[1, 3, 3],
             [2, 1, 4],
             [0, 6, 4]])
            ,
            12
        )
        self.assertEqual(grid.mineLeftToRightUpDown(
            [[1, 3, 1, 5],
            [2, 2, 4, 1],
            [5, 0, 2, 3],
            [0, 6, 1, 2]])
            ,
            16
        )
        self.assertEqual(grid.mineLeftToRightUpDown(
            [[10, 33, 13, 15],
            [22, 21, 4, 1],
            [5, 0, 2, 3],
            [0, 6, 14, 2]])
            ,
            83
        )

    def test_longestSnake(self):
        an1 = grid.AggregateNode(1)
        an2 = grid.AggregateNode(2)
        an2.endingMax = 3
        self.assertEqual(an1.endingMax, 1)
        self.assertEqual(an2.endingMax, 3)


        self.assertEqual(
            grid.longestSnake(
                [[9, 6, 5, 2],
                [8, 7, 6, 5],
                [7, 3, 1, 6],
                [1, 1, 1, 7]]
            ),
            7
        )

