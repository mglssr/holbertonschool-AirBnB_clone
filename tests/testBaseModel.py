#!/usr/bin/python3
"""Tests idk"""


import unittest
import uuid
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittests for the Base Model class"""

    def test_inst(self):
        """Tests if the instances of Base Model are correctly created"""
        base1 = BaseModel()
        base2 = BaseModel()

        self.assertNotEqual(base1.id, base2.id)
        self.assertNotEqual(base1.created_at, base2.created_at)
        self.assertNotEqual(base1.updated_at, base2.updated_at)
        self.assertIn(base1, storage.all().values())
        self.assertIn(base2, storage.all().values())

    def test_attr(self):
        """Tests is a new attribute of an instance is created"""
        my_base = BaseModel()
        my_base.name = "Rick Sanchez"
        my_base.my_number = 69
        my_base.save()

        self.assertEqual(my_base.name, "Rick Sanchez")
        self.assertEqual(my_base.my_number, 69)
        self.assertIn(my_base.name, my_base.to_dict().values())

    def test_type(self):
        """checks the types of the attributes"""
        base_ = BaseModel()
        base_.name = "Morty"
        base_.age = 15

        self.assertEqual(datetime, type(base_.updated_at))
        self.assertEqual(datetime, type(base_.created_at))
        self.assertEqual(str, type(base_.id))
        self.assertEqual(str, type(base_.name))

    def test_kwargs(self):
        """Checks if an instance can be created from a dictionary"""
        base = BaseModel()
        base.name = "Summer"
        base_json = base.to_dict()
        _json = base.to_dict()

        new_model = BaseModel(**base_json)
        new_model.name = "Pickle Rick"
        model_dict = new_model.to_dict()

        self.assertEqual(new_model.name, "Pickle Rick")
        self.assertNotEqual(new_model.name, "Summer")
        self.assertNotEqual(_json, model_dict)
        self.assertIn(new_model.name, model_dict.values())
        self.assertNotIn(base.name, model_dict.values())


if __name__ == '__main__':
    unnitest.main()
