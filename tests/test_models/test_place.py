#!/usr/bin/python3
"""test module for Place class"""


from models.place import Place
import unittest


class TestUser(unittest.TestCase):
    """test Place"""

    def test_class_name(self):
        """test class name"""
        self.assertEqual("Place", Place.class_name)


if __name__ == "__main__":
    unittest.main()
