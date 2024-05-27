#!/usr/bin/python3
"""

"""
import uuid
from datetime import datetime
import json


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        from. import storage           
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow().isoformat()
        self.updated_at = datetime.utcnow().isoformat()
        for key, value in kwargs.items():
            if key in ["created_at", "updated_at"]:
                setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
            else:
                setattr(self, key, value)

        storage.new(self)

    def save(self):
        """when instance is changed Update updated_at with current time 
        """
        from. import storage
        self.update_at = datetime.utcnow().isoformat()
        storage.save(self)

    def to_dict(self):
        """convert instance into dict f
        """
        inst_dict = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at
        dict_obj["updated_at"] = self.updated_at
        return dict_obj

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {json.dumps(self.__dict__, sort_keys=True)}"

