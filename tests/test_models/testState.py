#!/usr/bin/python3
"""Tests idk"""


import unittest
import models
from models.state import State
from models import storage
from datetime import datetime
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Unittests for the State class"""

    def test_subclass(self):
        """checks is State is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance(self):
        """Tests if the instances of User are correctly created"""
        S1 = State()
        S2 = State()

        self.assertNotEqual(S1.id, S2.id)
        self.assertNotEqual(S1.created_at, S2.created_at)
        self.assertNotEqual(S1.updated_at, S2.updated_at)
        self.assertIn(S1, storage.all().values())
        self.assertIn(S2, storage.all().values())
        self.assertEqual(State.name, "")


    def test_attr(self):
        """Tests is an attribute of an instance is created"""
        my_state = State()
        self.assertEqual(my_state.name, "")

if __name__ == '__main__':
    unittest.main()
