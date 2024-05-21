#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """Manages storage of hbnb models in JSON format in this class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """set in object with key"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Serialize objects to json file"""
        with open(FileStorage.__file_path, 'w') as fl:
            json.dump(self.__objects, fl)

    def reload(self):
        """Deserialize JSON file to __objects if the file exists"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fl:
                self.__objects = {k: YourClass.from_dict(v) for k, v in json.load(fl).items()}
