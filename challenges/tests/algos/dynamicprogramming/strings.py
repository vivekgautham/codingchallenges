
import unittest
from challenges.src.algos.dynamicprogramming import strings

class Test_Strings(unittest.TestCase):

    def test_Strings(self):
        self.assertTrue(strings.regularExpressionMatching("caab", "d*c*x*a*b"))
        self.assertTrue(strings.regularExpressionMatching("zab", "z.*"))
        self.assertFalse(strings.regularExpressionMatching("aaa", "aaaz"))