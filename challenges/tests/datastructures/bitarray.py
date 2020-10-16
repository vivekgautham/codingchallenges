
import unittest
from challenges.src.datastructures import bitarray


class Test_BitArray(unittest.TestCase):

    def test_checkDuplicates(self):
        self.assertTrue(bitarray.checkDuplicates([2, 3, 33, 64, 65, 32, 33]))
        self.assertTrue(bitarray.checkDuplicates([2, 3, 33, 64, 65, 32, 33]))
