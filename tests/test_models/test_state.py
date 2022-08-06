#!/usr/bin/python3
"""test module for State class"""


from models.state import State
import unittest


class TestUser(unittest.TestCase):
    """test State"""

    def test_class_name(self):
        """test class name"""
        self.assertEqual("State", State.__name__)


if __name__ == "__main__":
    unittest.main()
