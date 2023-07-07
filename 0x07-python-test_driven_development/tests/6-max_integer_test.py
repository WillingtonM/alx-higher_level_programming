#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test case for max_integer function"""

    def test_1(self):
        mtrx1 = [1,2,3,4]
        self.assertEqual(max_integer(mtrx1),4)

    def test_2(self):
        mtrx2 = []
        self.assertEqual(max_integer(mtrx2),None)

    def test_3(self):
        self.assertRaises(TypeError, max_integer,0)

    def test_4(self):
        mtrx4 = {5:'a',4:'b',3:'c'}
        self.assertRaises(KeyError, max_integer,mtrx4)

    def test_5(self):
        mtrx = ['a','b','c']
        self.assertEqual(max_integer(mtrx),'c')

    def test_6(self):
        mtrx = 'hello'
        self.assertEqual(max_integer(mtrx),'o')

    def test_7(self):
        mtrx = [-500,1,2,3]
        self.assertEqual(max_integer(mtrx),3)

    def test_8(self):
        mtrx1 = [4]
        self.assertEqual(max_integer(mtrx1),4)

    def test_9(self):
        mtrx1 = [4,1,2,3]
        self.assertEqual(max_integer(mtrx1),4)

    def test_10(self):
        mtrx1 = [1,2,6,5,4]
        self.assertEqual(max_integer(mtrx1),6)

if __name__ == '__main__':
    unittest.main()