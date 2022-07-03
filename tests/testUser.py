#!/usr/bin/python3
"""Tests idk"""


import unittest
import models
from models.user import User
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittests for the User class"""

    def test_inst(self):
        """Tests if the instances of User are correctly created"""
        User1 = User()
        User2 = User()

        self.assertNotEqual(User1.id, User2.id)
        self.assertNotEqual(User1.created_at, User2.created_at)
        self.assertNotEqual(User1.updated_at, User2.updated_at)
        self.assertIn(User1, storage.all().values())
        self.assertIn(User2, storage.all().values())

    def test_attr(self):
        """Tests is a new attribute of an instance is created"""
        my_User = User()
        my_User.email = "ricky_ricon@mail.com"
        my_User.password = 69696969
		
        my_User.save()

        self.assertEqual(my_User.email, "ricky_ricon@mail.com")
        self.assertEqual(my_User.password, 69696969)
        self.assertIn(my_User.email, my_User.to_dict().values())

    def test_type(self):
        """checks the types of the attributes"""
        user_ = User()
        user_.first_name = "Sam"
        user_.identifier = 25

        self.assertEqual(datetime, type(user_.updated_at))
        self.assertEqual(int, type(user_.identifier))
        self.assertEqual(str, type(user_.email))
        self.assertEqual(str, type(user_.first_name))

    def test_kwargs(self):
        """Checks if an instance can be created from a dictionary"""
        sup_user = User()
        sup_user.email = "summertime_sadness@mail.com"
        user_json = sup_user.to_dict()
        _json = sup_user.to_dict()

        new_model = User(**user_json)
        new_model.email = "outsider@mail.com"
        model_dict = new_model.to_dict()

        self.assertEqual(new_model.email, "outsider@mail.com")
        self.assertNotEqual(new_model.email, "summertime_sadness")
        self.assertNotEqual(_json, model_dict)
        self.assertIn(new_model.email, model_dict.values())
        self.assertNotIn(sup_user.email, model_dict.values())


if __name__ == '__main__':
    unnitest.main()
