#!/usr/bin/python3
"""Module for FileStorage class"""


import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        dctry = {}
        for key in self.__objects:
            dctry[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dctry, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                objts = json.load(f)
                for key, value in objts.items():
<<<<<<< HEAD
                    self.new
=======
                    self.new(eval(value['__class__'])(**value))
>>>>>>> d2a33db3305b3b6a8a8308c7172c62b6c0b6736b
