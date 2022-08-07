#!/usr/bin/python3
"""test module for User class"""


from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """test User"""

    def test_class_name(self):
        """test class name"""
        self.assertEqual("User", User.__name__)


if __name__ == "__main__":
    unittest.main()
