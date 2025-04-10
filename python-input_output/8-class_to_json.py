#!/usr/bin/python3
"""
A simple class to represent a person with attributes:
"""


import json


class MyClass:
    """
    A simple class to represent a person with attributes:
    name, age, and student status.
    """
    def __init__(self, name, age, is_student):
        """
        Initializes a MyClass instance with given attributes.
        
        param name: The name of the person.
        param age: The age of the person.
        param is_student: Boolean indicating whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def to_dict(self):
        """
        Converts the object's attributes into a dictionary.
        
        return: A dictionary representation of the object.
        """
        return {
            'name': self.name,
            'age': self.age,
            'is_student': self.is_student
        }

    def to_json(self):
        """
        Converts the object into a JSON string.
        
        return: JSON string representation of the object.
        """
        return json.dumps(self.to_dict())
