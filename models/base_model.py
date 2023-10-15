#!/usr/bin/python3
"""
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """THis Class for base model of object hierarchy."""

    def __init__(self, *args, **kwargs):
        """THis function Initialization of a Base instance.

        Args:
            - *args: This list of arguments
            - **kwargs: This dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for one in kwargs:
                if one == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif one == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[one] = kwargs[one]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """This function Returns a human-readable string representation
        of an instance."""

        return "[{}] ({}) {}".\
                format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """This function Updates the updated_at attribute
        with the current datetime."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This function Returns a dictionary representation of an instance."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
