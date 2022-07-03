#!/usr/bin/python3
"""Tests idk"""


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage


class TestAmenity(unittest.TestCase):
    """Unittests for the Amenity class"""

    def test_subclass(self):
        """checks is Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance(self):
        """Tests if the instances of User are correctly created"""
        A1 = Amenity()
        A2 = Amenity()

        self.assertNotEqual(A1.id, A2.id)
        self.assertNotEqual(A1.created_at, A2.created_at)
        self.assertNotEqual(A1.updated_at, A2.updated_at)
        self.assertIn(A1, storage.all().values())
        self.assertIn(A2, storage.all().values())
        self.assertEqual(Amenity.name, "")

    def test_attr(self):
        """Tests is an attribute of an instance is created"""
        a = Amenity()
        self.assertEqual(a.name, "")

if __name__ == '__main__':
    unittest.main()
