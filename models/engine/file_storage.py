#!/usr/bin/python3
"""file storage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        all method
            returns the class attribute __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        new method
            adds an instance of a class to the class attribute __objects
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        save method:
            saves to a json file
        """
        json_obj = FileStorage.__objects
        json_obj_data = {json_key: json_obj[json_key].to_dict()
                         for json_key in json_obj.keys()}
        json_obj_data_to_json = json.dumps(json_obj_data)
        with open(FileStorage.__file_path, "w") as json_file:
            json_file.write(json_obj_data_to_json)

    def reload(self):
        """
        reload method
            reload data from a json file
        """
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                py_dict = json.load(json_file)
                for val in py_dict.values():
                    cls_name = val["__class__"]
                    if cls_name == "BaseModel":
                        self.new(BaseModel(**val))
                    elif cls_name == "User":
                        self.new(User(**val))
                    elif cls_name == "Amenity":
                        self.new(Amenity(**val))
                    elif cls_name == "City":
                        self.new(City(**val))
                    elif cls_name == "Place":
                        self.new(Place(**val))
                    elif cls_name == "Review":
                        self.new(Review(**val))
                    elif cls_name == "State":
                        self.new(State(**val))
        except FileNotFoundError:
            return
