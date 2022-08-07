#!/usr/bin/python3
"""city module: contains the city class"""


from models.base_model import BaseModel


class City(BaseModel):
    """defines individual cities"""

    state_id = ""
    name = ""
