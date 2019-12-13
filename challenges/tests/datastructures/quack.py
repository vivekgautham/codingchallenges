import unittest
from challenges.src.datastructures import quack

class Test_Quack(unittest.TestCase):

    def test_quack(self):
        arr1, arr2, arr3 = [], [], []
        qk = quack.Quack(arr1, arr2, arr3)
        qk.push(23)
        qk.push(25)
        qk.push(34)
        qk.push(47)
        self.assertEquals(qk.pull(), 23)
        self.assertEquals(qk.pop(), 47)
        qk.push(38)
        self.assertEquals(qk.pop(), 38)
        self.assertEquals(qk.pull(), 25)        
        self.assertEquals(qk.pull(), 34)
        self.assertRaises(Exception, qk.pull)
        qk.push(1)
        self.assertEquals(qk.pop(), 1)
        self.assertRaises(Exception, qk.pop)
        qk.push(99)
        qk.push(75)
        self.assertEquals(qk.pop(), 75)
        self.assertEquals(qk.pull(), 99)




