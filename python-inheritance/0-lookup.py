#!/usr/bin/python3
def lookup(obj):
    """Returns the list of attributes and methods available for an object."""
    return dir(obj)


class Parent:
    def parent_method(self):
    pass

class Child(Parent):
    def child_method(self):
    pass


child_instance = Child()
print(dir(child_instance))
