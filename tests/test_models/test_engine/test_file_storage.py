#!/usr/bin/python3
"""Tests for File Storage"""


import unittest
from models.base_model import BaseModel
from models import storage
from models.user import User
import json

class TestFileStorage(unittest.TestCase):
    """Unittests for the File Storage"""

    def test_all(self):
        """Test all method"""
        base = BaseModel()
        all_storage = storage.all()
        self.assertIsNotNone(all_storage)
        self.assertEqual(all_storage, storage.all())
        self.assertIs(all_storage, storage.all())

    def test_new(self):
        """Test new method"""
        all_storage = storage.all()
        User_ = User()
        User_.name = "Patricio"
        user_id = User_.id
        storage.new(User_)
        self.assertIsNotNone(all_storage[User_.__class__.__name__ + "." + User_.id])

if __name__ == '__main__':
    unittest.main()
