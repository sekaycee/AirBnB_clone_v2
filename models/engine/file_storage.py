#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            a_dict = {}
            for key in self.__objects:
                part = key.replace('.', ' ')
                part = shlex.split(part)
                if (part[0] == cls.__name__):
                    a_dict[key] = self.__objects[key]
            return (a_dict)
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for key, val in self.__objects.items():
            temp[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                for key, val in (json.load(f)).items():
                    val = eval(val["__class__"])(**val)
                    self.__objects[key] = val
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete an existing object """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ calls reload() """
        self.reload()
