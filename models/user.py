#!/usr/bin/python3
"""This Module for User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """this Class representing a User."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""