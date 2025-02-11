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

    def to_json(self):
        """
        Converts the object into a dictionary representation.

        return: A dictionary containing the student's attributes.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
