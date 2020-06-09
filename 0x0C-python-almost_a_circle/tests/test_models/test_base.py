#!/usr/bin/python3
""" This module creates tests for Base
"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test for Base class"""

    def setUp(self):
        """setUp
        """
        Base._Base__nb_objects = 0
        self.a = Base()
        self.b = Base()
        self.c = Base(15)
        self.d = Base(12)
        self.e = Base("test")
        self.f = Base(5.5)
        self.g = Base()

    def tearDown(self):
        """tearDown
        """
        pass

    def test_simpleTest(self):
        """test_simpleTest
        """
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.b.id, 2)
        self.assertEqual(self.c.id, 15)
        self.assertEqual(self.d.id, 12)
        self.assertEqual(self.e.id, "test")
        self.assertEqual(self.f.id, 5.5)
        self.assertEqual(self.g.id, 3)

    def test_json_string(self):
        """test_json_string
        """
        r1 = Rectangle(5, 4, 1, 1, 1)
        r2 = Rectangle(2, 1, 0, 0, 2)
        my_dic_1 = r1.to_dictionary()
        my_dic_2 = r2.to_dictionary()
        jsonDic = Base.to_json_string([my_dic_1, my_dic_2])
        self.assertEqual(type(jsonDic), str)

    def test_json_string2(self):
        """test_json_string2
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        dic = r1.to_dictionary()
        jsonDic = Base.to_json_string([dic])
        list = json.loads(jsonDic)
        self.assertEqual(list, [dic])


if __name__ == '__main__':
    unittest.main()
