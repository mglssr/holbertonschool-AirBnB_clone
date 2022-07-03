#!/usr/bin/python3
"""Tests idk"""


import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os

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
        """checks the types of the attributes"""
        base_ = BaseModel()
        base_.name = "Morty"
        base_.age = 15

        self.assertIs(datetime, type(base_.updated_at))
        self.assertIs(datetime, type(base_.created_at))
        self.assertIs(str, type(base_.id))
        self.assertEqual(int, type(base_.age))
        self.assertIn(base_.name, base_.to_dict().values())

    def test__str__(self):
        """Test the __str__ method"""
        b = BaseModel()
        self.assertEqual(f"[{type(b).__name__}] ({b.id}) {b.__dict__}", str(b))

    def test_save(self):
        """Test the save method"""
        c = BaseModel()
        updated_at = c.__dict__['updated_at']
        c.save()
        self.assertNotEqual(c.__dict__['updated_at'], updated_at)
        self.assertTrue(os.path.isfile('file.json'))
        new_updated_at = c.__dict__['updated_at']
        storage.reload()
        self.assertEqual(c.__dict__['updated_at'], new_updated_at)

    def test_to_dict(self):
        """tests to_dict method"""
        d = BaseModel()
        ddic = d.to_dict()
        self.assertEqual(ddic["id"], d.id)
        self.assertEqual(ddic["created_at"], d.created_at.isoformat())
        self.assertEqual(ddic["updated_at"], d.updated_at.isoformat())
        self.assertEqual(ddic['__class__'], d.__class__.__name__)
    
if __name__ == '__main__':
    unittest.main()
