#!/usr/bin/python3
"""Tests idk"""


import unittest
import models
from models.amenity import Amenity
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittests for the Amenity class"""

    def test_inst(self):
        """Tests if the instances of Amenity are correctly created"""
        a = Amenity()
        b = Amenity()

        self.assertNotEqual(a.id, b.id)
        self.assertNotEqual(a.created_at, b.created_at)
        self.assertNotEqual(a.updated_at, b.updated_at)
        self.assertIn(a, storage.all().values())
        self.assertIn(b, storage.all().values())

    def test_attr(self):
        """Tests is a new attribute of an instance is created"""
        a = Amenity()
        a.name = "Piss City"
        a.num = 126
        a.save()

        self.assertEqual(a.name, "Piss City")
        self.assertEqual(a.num, 126)
        self.assertIn(a.name, a.to_dict().values())

    def test_type(self):
        """checks the types of the attributes"""
        b_ = Amenity()
        b_.name = "The Rocks"
        b_.num = 1515

        self.assertEqual(datetime, type(b_.updated_at))
        self.assertEqual(datetime, type(b_.created_at))
        self.assertEqual(int, type(b_.num))
        self.assertEqual(str, type(b_.name))

    def test_kwargs(self):
        """Checks if an instance can be created from a dictionary"""
        c = Amenity()
        c.name = "Monte Sexto de este a oeste"
        base_json = c.to_dict()
        _json = c.to_dict()

        new_model = Amenity(**base_json)
        new_model.name = "Montevideo"
        model_dict = new_model.to_dict()

        self.assertEqual(new_model.name, "Montevideo")
        self.assertNotEqual(new_model.name, "Monte Sexto de este a oeste")
        self.assertNotEqual(_json, model_dict)
        self.assertIn(new_model.name, model_dict.values())
        self.assertNotIn(c.name, model_dict.values())


if __name__ == '__main__':
    unnitest.main()
