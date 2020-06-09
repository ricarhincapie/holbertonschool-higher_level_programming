#!/usr/bin/python3
""" This module creates tests for Base
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test for Rectangle class"""

    def setUp(self):
        """Set up"""
        self.c = Rectangle(2, 2)

    def test_rectangle(self):
        """test_rectangle test cases for rectangle Class
        """
        a = Rectangle(10, 20)
        self.assertEqual(a.id, 2)
        self.assertEqual(a.width, 10)
        b = Rectangle(5, 10, 2, 2, 24)
        self.assertEqual(b.x, 2)
        self.assertEqual(b.id, 24)
        self.assertIsInstance(b, Rectangle)
        b.height = 15
        self.assertEqual(b.height, 15)
        b.y = 10
        self.assertEqual(b.y, 10)
        # AT __STR__
        # self.assertEqual(a.__str__, "[Rectangle] (1) 0/0 - 10/20")
        # AT DISPLAY()
        self.assertIsNone(self.c.display())
        # self.assertEqual(c.display(), "[[##], [##]]")
        # AT UPDATE()
        b.update(1, 2, 3, 4, 5)
        self.assertEqual(b.y, 5)
        b.update(width=20)
        self.assertEqual(b.width, 20)

    def test_rectangle_to_dictionary(self):
        """test_rectangle_to_dictionary
        """
        b = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(b.to_dictionary(), dict)
        self.assertNotIsInstance(b.to_dictionary(), list)

    def test_rectangle_area(self):
        """Test area method
        """
        a = Rectangle(10, 20)
        self.assertEqual(a.area(), 200)
        self.assertIsInstance(a.area(), int)

    def test_rectangle_errors_init(self):
        """test_rectangle_errors_init tests errors at init
        """
        with self.assertRaises(TypeError):
            Rectangle("2", 20)
            Rectangle([2, 1], 3)
        with self.assertRaises(ValueError):
            Rectangle(2, 3, -1, 0, 1)
            d = Rectangle(0, 10)

    def test_rectangle_errors_setter(self):
        """test_rectangle_errors_setter
        """
        # c = Rectangle(2, 2)
        with self.assertRaises(TypeError):
            self.c.width = [1]
        with self.assertRaises(ValueError):
            self.c.y = -1

    def test_rectangle_errors_update(self):
        """test_rectangle_errors_update
        """
        with self.assertRaises(TypeError):
            self.c.update(1, "2")
            self.c.update(1, [1])

        self.c.update(mama=20)
        with self.assertRaises(AttributeError):
            self.c.mama

if __name__ == '__main__':
    unittest.main()
