import unittest
from challenges.src.miscellaneous import accounting

class Test_Accounting(unittest.TestCase):

    def test_TaxesOwed(self):
        self.assertEqual(accounting.taxesOwed(5000), 500.0)
        self.assertEqual(accounting.taxesOwed(10000), 1009.5)
        self.assertEqual(accounting.taxesOwed(20000), 2209.5)
        self.assertEqual(accounting.taxesOwed(30000), 3409.5)
        self.assertEqual(accounting.taxesOwed(40000), 4739.5)
        self.assertEqual(accounting.taxesOwed(50000), 6939.5)

if __name__ == '__main__':
    unittest.main()