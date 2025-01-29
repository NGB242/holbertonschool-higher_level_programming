#!/usr/bin/python3
class Rectangle:
    # Init function
    def __init__(self):
        # The only members are length and width
        self.length = 1
        self.width = 1

    # Setters
    def set_width(self, width):
        self.width = width

    def set_length(self, length):
        self.length = length

    # Getters
    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_area(self):
        return self.length * self.width

    # String representation
    def __str__(self):
        return 'length = {}, width = {}'.format(self.length, self.width)
