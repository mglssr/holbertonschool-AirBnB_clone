#!/usr/bin/python3
"""Tests idk"""


import unittest
import models
from models.review import Review
from models.base_model import BaseModel
from models import storage


class TestReview(unittest.TestCase):
    """Unittests for the Review class"""

    def test_subclass(self):
        """checks is Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance(self):
        """Tests if the instances of User are correctly created"""
        R1 = Review()
        R2 = Review()

        self.assertNotEqual(R1.id, R2.id)
        self.assertNotEqual(R1.created_at, R2.created_at)
        self.assertNotEqual(R1.updated_at, R2.updated_at)
        self.assertIn(R1, storage.all().values())
        self.assertIn(R2, storage.all().values())
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")


    def test_attr(self):
        """Tests is an attribute of an instance is created"""
        my_review = Review()
		
        self.assertEqual(my_review.place_id, "")
        self.assertEqual(my_review.user_id, "")
        self.assertEqual(my_review.text, "")

if __name__ == '__main__':
    unittest.main()
