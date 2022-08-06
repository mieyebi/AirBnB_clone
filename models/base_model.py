#!/usr/bin/python3
"""class BaseModel is the parent class of all classes
in this package"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class: all classes inherits this"""

    # class_name = "BaseModel"

    def __init__(self, *args, **kwargs):
        if kwargs:
            for item in kwargs:
                if item != "__class__":
                    self.__dict__[item] = kwargs[item]
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """updates updated_at attribute to current
         date"""
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """string representation of instance"""
        string = "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id,
                                       self.__dict__)
        return string

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        dct = {}
        to_copy = self.__dict__
        for item in to_copy:
            dct[item] = to_copy[item]

        dct["__class__"] = self.__class__.__name__
        dct["created_at"] = self.created_at.isoformat()
        dct["updated_at"] = self.updated_at.isoformat()
        return dct
