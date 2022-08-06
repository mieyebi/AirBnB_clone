#!/usr/bin/python3
"""test module for Amenity class"""


from models.amenity import Amenity
import unittest


class TestUser(unittest.TestCase):
    """test User"""

    def test_class_name(self):
        """test class name"""
        self.assertEqual("Amenity", Amenity.__name__)


if __name__ == "__main__":
    unittest.main()
