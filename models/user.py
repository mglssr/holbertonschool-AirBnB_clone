#!/usr/bin/python3
"""Module for User class"""


from models.base_model import BaseModel


def class User(BaseModel):
    """User class"""
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
