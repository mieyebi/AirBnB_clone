#!/usr/bin/python3
"""test module for BaseModel class"""


from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """test BaseModel"""

    def test_class_name(self):
        """test class name"""
        self.assertEqual("BaseModel", BaseModel.class_name)


if __name__ == "__main__":
    unittest.main()
