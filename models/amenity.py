#!/usr/bin/python3
"""amenity module: contains Amenity class"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """defines amenities"""

    class_name = "Amenity"
    name = ""
