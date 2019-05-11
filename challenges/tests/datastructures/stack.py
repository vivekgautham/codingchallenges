import unittest
from challenges.src.datastructures import stack


class Test_Stack(unittest.TestCase):

    def test_stack(self):
        s = stack.Stack()
        s.push(23)
        s.push(25)
        s.push(34)
        s.push(47)
        self.assertEqual(s.pop(), 47)
        self.assertEqual(s.pop(), 34)
        self.assertEqual(s.pop(), 25)
        self.assertEqual(s.pop(), 23)
        s.push(98)
        s.push(12)
        self.assertEqual(s.pop(), 12)
        s.push(96)
        self.assertEqual(s.pop(), 96)
        self.assertEqual(s.pop(), 98)

if __name__ == '__main__':
    unittest.main()
