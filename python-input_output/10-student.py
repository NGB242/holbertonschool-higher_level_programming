#!/usr/bin/python3
"""
A class representing a student with first name, last name, and age.
"""


class Student:
    """
    A class representing a student with first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with given attributes.

        param first_name: The first name of the student.
        param last_name: The last name of the student.
        param age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student.
        param attrs: A list of attribute names to include,
         in the dictionary.
        If None, all attributes are included.
        return: A dictionary containing the specified,
        attributes of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items()if k in attrs}
