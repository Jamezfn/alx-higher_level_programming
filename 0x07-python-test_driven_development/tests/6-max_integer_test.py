#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer function"""
    def test_ordered_list(self):
        """Ordered list"""
        my_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(my_list), 4)

    def test_unordered_list(self):
        """Unordered list"""
        my_list = [3, 1, 4, 2]
        self.assertEqual(max_integer(my_list), 4)

    def test_max_beginning(self):
        """Value at the beginning of the list"""
        my_list = [10, 9, 2, 5]
        self.assertEqual(max_integer(my_list), 10)

    def test_floats_list(self):
        """Test a list with floats"""
        my_list = [10.1, 10.2, 10.3, 10.4]
        self.assertEqual(max_integer(my_list), 10.4)

    def test_floatsAdInt(self):
        """Test a mix of floats and int"""
        my_list = [10.1, 10, 9, 9.1]
        self.assertEqual(max_integer(my_list), 10.1)

    def test_empty_list(self):
        """Test with empty list"""
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_char(self):
        """Test with a list of characters"""
        my_list = ['a', 'b', 'c', 'd']
        self.assertEqual(max_integer(my_list), 'd')
    def test_string(self):
        """Test with a string"""
        my_list = 'james'
        self.assertEqual(max_integer(my_list), 's')

    def test_emptyString(self):
        """Test with empty string"""
        self.assertEqual(max_integer(""), None)

    def test_oneInt(self):
        """Test with a list of only one int"""
        my_list = [7]
        self.assertEqual(max_integer(my_list), 7)

if __name__ == '__main__':
    unnitest.main()
