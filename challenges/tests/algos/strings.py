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

    def test_longestPalindromeSubstrAlternative(self):
        self.assertEqual(strings.longestPalindromeSubstrAlternative("bananas"), "anana")
        self.assertEqual(strings.longestPalindromeSubstrAlternative("aabcdcb"), "bcdcb")
        self.assertEqual(strings.longestPalindromeSubstrAlternative("aba"), "aba")
        self.assertEqual(strings.longestPalindromeSubstrAlternative("abba"), "abba")
        self.assertEqual(strings.longestPalindromeSubstrAlternative("abcd"), "")

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

    def test_smallestWindowContainingAllDistinctChars(self):
        self.assertEqual(strings.smallestWindowContainingAllDistinctChars("jiujitsu"), 5)
        self.assertEqual(strings.smallestWindowContainingAllDistinctChars("caabcckbssaka"), 6)
        self.assertEqual(strings.smallestWindowContainingAllDistinctChars("aabcbcdbca"), 4)
        self.assertEqual(strings.smallestWindowContainingAllDistinctChars("acaadacdca"), 3)

    def test_smallestWindowContainingAllDistinctCharsOptimized(self):
        self.assertEqual(strings.smallestWindowContainingAllDistinctCharsOptimized("xyyzyzyx"), 3)
        self.assertEqual(strings.smallestWindowContainingAllDistinctCharsOptimized("jiujitsu"), 5)
        self.assertEqual(strings.smallestWindowContainingAllDistinctCharsOptimized("caabcckbssaka"), 6)
        self.assertEqual(strings.smallestWindowContainingAllDistinctCharsOptimized("aabcbcdbca"), 4)
        self.assertEqual(strings.smallestWindowContainingAllDistinctCharsOptimized("acaadacdca"), 3)

    def test_largestSubStrContainingAtmostKDistinctChars(self):
        self.assertEqual(strings.largestSubStrContainingAtmostKDistinctChars("abcba", 2), "bcb")
        self.assertEqual(strings.largestSubStrContainingAtmostKDistinctChars("acaadacdca", 2), "acaa")
        self.assertEqual(strings.largestSubStrContainingAtmostKDistinctChars("acaadacdca", 3), "acaadacdca")
        self.assertEqual(strings.largestSubStrContainingAtmostKDistinctChars("caabcckbssaka", 1), "aa")
        self.assertEqual(strings.largestSubStrContainingAtmostKDistinctChars("caabcckbssaka", 2), "caa")
        self.assertEqual(strings.largestSubStrContainingAtmostKDistinctChars("caabcckbssaka", 3), "caabcc")

    def test_reverseWordsBetweenDelimiters(self):
        self.assertEqual(strings.reverseWordsBetweenDelimiters("hello//world:here", {'/', ':'}), "here//world:hello")
        self.assertEqual(strings.reverseWordsBetweenDelimiters("hello/world:here", {'/', ':'}), "here/world:hello")
        self.assertEqual(strings.reverseWordsBetweenDelimiters("hello/world:here/", {'/', ':'}), "here/world:hello/")


    def test_repeatedStringMatching(self):
        self.assertEqual(strings.repeatedStringMatch('aab', 'ba'), 2)
        self.assertEqual(strings.repeatedStringMatch('cda', 'ba'), -1)
        self.assertEqual(strings.repeatedStringMatch('dca', 'adcadcadc'), 4)
        self.assertEqual(strings.repeatedStringMatch('pda', 'apd'), 2)

    def test_minimumAdjSwapsToAnagram(self):
        self.assertEqual(strings.minimumAdjSwapsToAnagram('abcd', 'cdab'), 4)
        self.assertEqual(strings.minimumAdjSwapsToAnagram('abcfdegji', 'fjiacbdge'), 17)
        self.assertEqual(strings.minimumAdjSwapsToAnagram('acdas', 'saadc'), 7)

    def test_canStringBeMadeIntoPalindrome(self):
        self.assertTrue(strings.canStringBeMadeIntoPalindrome('slsaals'))
        self.assertFalse(strings.canStringBeMadeIntoPalindrome('post'))
        self.assertTrue(strings.canStringBeMadeIntoPalindrome('sammas'))
        self.assertTrue(strings.canStringBeMadeIntoPalindrome('massa'))

if __name__ == '__main__':
    unittest.main()