#!/usr/bin/env python3
"""
Initialize the attributes of the custom object
"""


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):

        """
        Initialize the attributes of the custom object.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object.
        """
        print(f"Name: {self.name}, Age: {self.age}, Is Student: {self.is_student}")


    def serialize(self, filename):
        """
        Serialize the object and save it to the specified file.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)


    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of CustomObject from the specified file.
        """
        with open(filename, 'rb') as file:
            return pickle.load(file)
