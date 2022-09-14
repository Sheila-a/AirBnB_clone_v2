#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os
from .amenity import Amenity
from .place import Place
from .city import City
from .state import State
from .review import Review
from .user import User

s = os.getenv('HBNB_TYPE_STORAGE')
storage = None
if s == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
