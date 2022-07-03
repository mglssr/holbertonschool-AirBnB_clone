#!/usr/bin/python3
"""Tests idk"""


import unittest
import models
from models.user import User
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittests for the User class"""

    def issubclass(self):
        """checks is User is a subclass of BaseModel"""
        self.assertEqual(User, BaseModel)

    def test_inst(self):
        """Tests if the instances of User are correctly created"""
        User1 = User()
        User2 = User()

        self.assertNotEqual(User1.id, User2.id)
        self.assertNotEqual(User1.created_at, User2.created_at)
        self.assertNotEqual(User1.updated_at, User2.updated_at)
        self.assertIn(User1, storage.all().values())
        self.assertIn(User2, storage.all().values())
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")


    def test_attr(self):
        """Tests is an attribute of an instance is created"""
        my_User = User()
		
        self.assertEqual(my_User.email, "")
        self.assertEqual(my_User.password, "")
        self.assertEqual(my_User.first_name, "")
        self.assertEqual(my_User.last_name, "")

if __name__ == '__main__':
    unnitest.main()
