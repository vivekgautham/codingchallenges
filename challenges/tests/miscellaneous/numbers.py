import unittest
from challenges.src.miscellaneous import numbers

class Test_Numbers(unittest.TestCase):

    def test_longDivision(self):
        self.assertEqual(numbers.longDivision(1, 2),  "0.5")
        self.assertEqual(numbers.longDivision(1, 56), "0.017(857142)")
        self.assertEqual(numbers.longDivision(1, 3),  "0.(3)")
        self.assertEqual(numbers.longDivision(22, 7),  "3.(142857)")

    def test_gcd(self):
        self.assertEqual(numbers.gcd(2, 3), 1)
        self.assertEqual(numbers.gcd(2, 4), 2)
        self.assertEqual(numbers.gcd(24, 9), 3)
        self.assertEqual(numbers.gcd(42, 56), 14)
        self.assertEqual(numbers.gcd(24, 12), 12)
        self.assertEqual(numbers.gcd(22, 12), 2)

    def test_gcdInBulk(self):
        self.assertEqual(numbers.gcdInBulk([14, 42, 56]), 14)
        self.assertEqual(numbers.gcdInBulk([28, 56, 112]), 28)
        self.assertEqual(numbers.gcdInBulk([2, 3, 5]), 1)

    def test_intToRoman(self):
        self.assertEqual(numbers.intToRoman(3549), 'MMMDXLIX')
        self.assertEqual(numbers.intToRoman(41), 'XLI')
        self.assertEqual(numbers.intToRoman(44), 'XLIV')
        self.assertEqual(numbers.intToRoman(45), 'XLV')


    def test_romanToInt(self):
        self.assertEqual(numbers.romanToInt('MMMDXLIX'), 3549)
        self.assertEqual(numbers.romanToInt('XLI'), 41)
        self.assertEqual(numbers.romanToInt('XLIV'), 44)
        self.assertEqual(numbers.romanToInt('XLV'), 45)

    def test_highestPossibleNumberFromArray(self):
        self.assertEqual(numbers.highestPossibleNumberFromArray([10, 7, 76, 415]), 77641510)
        self.assertEqual(numbers.highestPossibleNumberFromArray([10, 7, 76, 766]), 77676610)
        self.assertEqual(numbers.highestPossibleNumberFromArray([10, 7, 76, 767]), 77677610)
        self.assertEqual(numbers.highestPossibleNumberFromArray([10, 7, 78, 76, 415]), 7877641510)
        self.assertEqual(numbers.highestPossibleNumberFromArray([54, 546, 548, 60]), 6054854654)
        self.assertEqual(numbers.highestPossibleNumberFromArray([1, 34, 3, 98, 9, 76, 45, 4]), 998764543431)









