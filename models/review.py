#!/usr/bin/python3
"""review module: contains Review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """defines individual cities"""

    class_name = "Review"
    place_id = ""
    user_id = ""
    text = ""
