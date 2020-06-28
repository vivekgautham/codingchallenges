import unittest
from challenges.src.miscellaneous import numbers

class Test_Numbers(unittest.TestCase):

    def test_longDivision(self):
        self.assertEqual(numbers.longDivision(1, 2),  "0.5")
        self.assertEqual(numbers.longDivision(1, 56), "0.017(857142)")
        self.assertEqual(numbers.longDivision(1, 3),  "0.(3)")
        self.assertEqual(numbers.longDivision(22, 7),  "3.(142857)")


