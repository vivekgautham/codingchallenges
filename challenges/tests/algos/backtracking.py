
from challenges.src.algos import backtracking

import unittest

class Test_BackTracking(unittest.TestCase):

    def test_nQueens(self):
        self.assertEqual(backtracking.nQueens(9), 352)
        self.assertEqual(backtracking.nQueens(8), 92)
        self.assertEqual(backtracking.nQueens(0), 0)
        self.assertEqual(backtracking.nQueens(1), 1)
        self.assertEqual(backtracking.nQueens(2), 0)
        self.assertEqual(backtracking.nQueens(3), 0)
        self.assertEqual(backtracking.nQueens(4), 2)
        self.assertEqual(backtracking.nQueens(5), 10)
        self.assertEqual(backtracking.nQueens(6), 4)
        self.assertEqual(backtracking.nQueens(7), 40)

    def test_Itinerary(self):
        self.assertEqual(backtracking.itinerary(
            [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')],
            ['YUL']),
            ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
        )
        self.assertEqual(backtracking.itinerary(
            [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')],
            ['A']),
            ['A', 'B', 'C', 'A', 'C']
        )

        self.assertEqual(backtracking.itinerary(
            [('SFO', 'COM'), ('COM', 'YYZ')],
            ['COM']),
            None
        )

    def test_sumSubSet(self):
        self.assertEqual(backtracking.sumSubset([12, 1, 61, 5, 9, 2], 24), [[12, 1, 9, 2]])

    def test_SudokuSolver(self):
        completeBoard = [
                [3, 1, 6, 5, 7, 8, 4, 9, 2,],
                [5, 2, 9, 1, 3, 4, 7, 6, 8,],
                [4, 8, 7, 6, 2, 9, 5, 3, 1,],
                [2, 6, 3, 4, 1, 5, 9, 8, 7,],
                [9, 7, 4, 8, 6, 3, 1, 2, 5,],
                [8, 5, 1, 7, 9, 2, 6, 4, 3,],
                [1, 3, 8, 9, 4, 7, 2, 5, 6,],
                [6, 9, 2, 3, 5, 1, 8, 7, 4,],
                [7, 4, 5, 2, 8, 6, 3, 1, 9,]
            ]
        solver = backtracking.SudokuSolver(
            completeBoard
        )
        self.assertTrue(solver._isValidSoFar())
        self.assertTrue(solver._isComplete())

        board  = [
                [3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0]
            ]
        solver = backtracking.SudokuSolver(
            board
        )
        self.assertTrue(solver._isValidSoFar())
        resBoard = solver.solve()
        self.assertEquals(resBoard, completeBoard)


if __name__ == '__main__':
    unittest.main()

