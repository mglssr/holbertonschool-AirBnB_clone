#!/usr/bin/python3
"""Tests idk"""


import unittest
import models
from models.city import City
from models import storage
from datetime import datetime
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unittests for the City class"""

    def test_subclass(self):
        """checks is City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_inst(self):
        """Tests if the instances of User are correctly created"""
        C1 = City()
        C2 = City()

        self.assertNotEqual(C1.id, C2.id)
        self.assertNotEqual(C1.created_at, C2.created_at)
        self.assertNotEqual(C1.updated_at, C2.updated_at)
        self.assertIn(C1, storage.all().values())
        self.assertIn(C2, storage.all().values())
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")


    def test_attr(self):
        """Tests is an attribute of an instance is created"""
        my_city = City()
        self.assertEqual(my_city.state_id, "")
        self.assertEqual(my_city.name, "")

if __name__ == '__main__':
    unittest.main()
