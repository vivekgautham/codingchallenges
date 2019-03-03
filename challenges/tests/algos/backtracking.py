
from challenges.src.algos import backtracking

import unittest

class Test_BackTracking(unittest.TestCase):

    def test_nQueens(self):
        self.assertEqual(backtracking.nQueens(9), 352)
        self.assertEqual(backtracking.nQueens(8), 92)
        self.assertEqual(backtracking.nQueens(0), 1)
        self.assertEqual(backtracking.nQueens(1), 1)

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
        
if __name__ == '__main__':
    unittest.main()

