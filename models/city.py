#!/usr/bin/python3
"""city module: contains city class"""


from models.base_model import BaseModel


class City(BaseModel):
    """defines individual cities"""

    class_name = "City"
    state_id = ""
    name = ""
