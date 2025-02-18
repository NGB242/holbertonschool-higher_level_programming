#!/usr/bin/python3
"""
Initialize the attributes of the custom object
"""


import pickle


class CustomObject:
    def __init__(self,    name,    age,    is_student):

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
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to the specified file.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            """
            Handle any exceptions that occur during serialization.
            """
            print(f"Serialization error: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of CustomObject from the specified file.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            """
            Handle any exceptions that occur during deserialization.
            """
            print(f"Deserialization error: {e}")
            return None
