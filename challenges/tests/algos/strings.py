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

    def test_isPalindromeProducibleNaive(self):
        self.assertEqual(strings.isPalindromeProducibleNaive("waterrfetawx", 2), True)
        self.assertEqual(strings.isPalindromeProducibleNaive("waterrfetawx", 1), False)
        self.assertEqual(strings.isPalindromeProducibleNaive("aabbccdd", 2), False)
        self.assertEqual(strings.isPalindromeProducibleNaive("acbkbda", 2), True)
        self.assertEqual(strings.isPalindromeProducibleNaive("acbkbda", 1), False)
        self.assertEqual(strings.isPalindromeProducibleNaive("malayalam", 0), True)
        self.assertEqual(strings.isPalindromeProducibleNaive("malayalam", 1), True)

    def test_isPalindromeProducible(self):
        self.assertEqual(strings.isPalindromeProducible("waterrfetawx", 2), True)
        self.assertEqual(strings.isPalindromeProducible("waterrfetawx", 1), False)
        self.assertEqual(strings.isPalindromeProducible("aabbccdd", 2), False)
        self.assertEqual(strings.isPalindromeProducible("acbkbda", 2), True)
        self.assertEqual(strings.isPalindromeProducible("acbkbda", 1), False)
        self.assertEqual(strings.isPalindromeProducible("malayalam", 0), True)
        self.assertEqual(strings.isPalindromeProducible("malayalam", 1), True)
        self.assertEqual(strings.isPalindromeProducible("aabckcda", 1), False)
        self.assertEqual(strings.isPalindromeProducible("aabckcda", 2), False)
        self.assertEqual(strings.isPalindromeProducible("aabckcda", 3), True)
        self.assertEqual(strings.isPalindromeProducible("abcdecba", 0), False)
        self.assertEqual(strings.isPalindromeProducible("abcdecba", 1), True)

        self.assertEqual(strings.isPalindromeProducible("abcdeca", 0), False)
        self.assertEqual(strings.isPalindromeProducible("abcdeca", 1), False)
        self.assertEqual(strings.isPalindromeProducible("abcdeca", 2), True)
        self.assertEqual(strings.isPalindromeProducible("acdcb", 0), False)
        self.assertEqual(strings.isPalindromeProducible("acdcb", 1), False)
        self.assertEqual(strings.isPalindromeProducible("acdcb", 2), True)


if __name__ == '__main__':
    unittest.main()