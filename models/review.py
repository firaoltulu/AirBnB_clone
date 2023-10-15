#!/usr/bin/python3
"""This Module for Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """This Class representing a Review."""
    place_id = ""
    user_id = ""
    text = ""
