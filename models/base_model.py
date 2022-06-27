#!/usr/bin/python3
"""Module for BaseModel class"""


import json
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self):
        self.id = uuid.uuid4()
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """Returns the string representation of the model"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates update_at with the current datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        return self.__dict__
