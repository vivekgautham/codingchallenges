import unittest
from challenges.src.algos.huffman import HuffmanTree

class Test_Huffman(unittest.TestCase):

    def test_HuffmanEncoding(self):
        ht = HuffmanTree(['a', 'b', 'c', 'd', 'e', 'f'], [5, 9, 12, 13, 16, 45])
        ht.computeCodes()
        self.assertEqual(ht.codes,
            {
                'f': '0',
                'c': '100',
                'd': '101',
                'a': '1100',
                'b': '1101',
                'e': '111'
            }
        )


if __name__ == '__main__':
    unittest.main()
