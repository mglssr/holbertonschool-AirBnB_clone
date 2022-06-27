#!/usr/bin/python3
"""
    module
"""


import json
from datetime import datetime
import uuid
import time

class BaseModel:
    
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.update_at = datetime.now()
