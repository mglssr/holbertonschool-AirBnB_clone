#!/usr/bin/python3
"""Tests idk"""


import unittest
import models
from models.place import Place
from models.base_model import BaseModel
from models import storage


class TestPlace(unittest.TestCase):
    """Unittests for the Place class"""

    def test_subclass(self):
        """checks is Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_instance(self):
        """Tests if the instances of User are correctly created"""
        P1 = Place()
        P2 = Place()

        self.assertNotEqual(P1.id, P2.id)
        self.assertNotEqual(P1.created_at, P2.created_at)
        self.assertNotEqual(P1.updated_at, P2.updated_at)
        self.assertIn(P1, storage.all().values())
        self.assertIn(P2, storage.all().values())
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, ())


    def test_attr(self):
        """Tests is an attribute of an instance is created"""
        my_place = Place()
        self.assertEqual(my_place.city_id, "")
        self.assertEqual(my_place.user_id, "")
        self.assertEqual(my_place.name, "")
        self.assertEqual(my_place.description, "")
        self.assertEqual(my_place.number_rooms, 0)
        self.assertEqual(my_place.number_bathrooms, 0)
        self.assertEqual(my_place.max_guest, 0)
        self.assertEqual(my_place.price_by_night, 0)
        self.assertEqual(my_place.latitude, 0.0)
        self.assertEqual(my_place.longitude, 0.0)
        self.assertEqual(my_place.amenity_ids, ())

if __name__ == '__main__':
    unittest.main()
