#!/usr/bin/python3
"""test module for City class"""


from models.city import City
import unittest


class TestUser(unittest.TestCase):
    """test City"""

    def test_class_name(self):
        """test class name"""
        self.assertEqual("City", City.__name__)


if __name__ == "__main__":
    unittest.main()
