#!/usr/bin/python3
"""module contains class FileStorage that serialization and
deserialization of object instances to and from a file"""


import json


class FileStorage:
    """serves to persist objects to disc and retrieve objects from
    disc"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        name = obj.__class__.__name__
        key = "{}.{}".format(name, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            dct = {}
            for item in self.__objects:
                dct[item] = self.__objects[item].to_dict()
            f.write(json.dumps(dct))

    def reload(self):
        """deserializes the JSON file to __objects"""
        # import os
        # if (os.path.isfile(self.__file_path)):
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                dct = json.loads(f.read())
                self.__objects = {}
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                for item in dct:
                    # item is key and has structure of <class name>.id
                    cls = item.split(".")[0]
                    if cls == "BaseModel":
                        self.__objects[item] = BaseModel(**dct[item])
                    elif cls == "User":
                        self.__objects[item] = User(**dct[item])
                    elif cls == "State":
                        self.__objects[item] = State(**dct[item])
                    elif cls == "City":
                        self.__objects[item] = City(**dct[item])
                    elif cls == "Amenity":
                        self.__objects[item] = Amenity(**dct[item])
                    elif cls == "Place":
                        self.__objects[item] = Place(**dct[item])
                    elif cls == "Review":
                        self.__objects[item] = Review(**dct[item])
        except Exception:
            pass
