import unittest
from challenges.src.algos import strings

class Test_String(unittest.TestCase):

    def test_LongestSubstringWithKDistinctCharacters(self):
        pass

    def test_LevnshteinDistance(self):
        self.assertEqual(strings.levenshteinDistance("kitten", "sitting"), 3)
        self.assertEqual(strings.levenshteinDistance("kitten", "cat"), 5)
        self.assertEqual(strings.levenshteinDistance("black", "white"), 5)
        self.assertEqual(strings.levenshteinDistance("top", "dog"), 2)

    def test_longestPalindromeSubstr(self):
       self.assertEqual(strings.longestPalindromeSubstr("bananas"), "anana")
       self.assertEqual(strings.longestPalindromeSubstr("aabcdcb"), "bcdcb")
       self.assertEqual(strings.longestPalindromeSubstr("aba"), "aba")
       self.assertEqual(strings.longestPalindromeSubstr("abba"), "abba")
       self.assertEqual(strings.longestPalindromeSubstr("abcd"), "")

if __name__ == '__main__':
    unittest.main()