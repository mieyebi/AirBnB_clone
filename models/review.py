#!/usr/bin/python3
"""review module: contains the Review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """defines individual cities"""

    place_id = ""
    user_id = ""
    text = ""
