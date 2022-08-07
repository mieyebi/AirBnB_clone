#!/usr/bin/python3
"""test module for Review class"""


from models.review import Review
import unittest


class TestUser(unittest.TestCase):
    """test Review"""

    def test_class_name(self):
        """test class name"""
        self.assertEqual("Review", Review.__name__)


if __name__ == "__main__":
    unittest.main()
