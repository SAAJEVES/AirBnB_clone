#!/usr/bin/python3
"""a classe that inherit from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class"""
    state_id = ""
    name = ""
