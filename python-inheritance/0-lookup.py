#!/usr/bin/python3
def lookup(obj):
    """Returns the list of attributes and methods available for an object."""
    return dir(obj)


class Parent: 

    """ Definition of the Parent class """
    
    def parent_method(self): 
        """ Parent class method """
    pass
    """ This method does nothing for the moment"""

class Child(Parent):

    """ Definition of the Child class, which inherits from Parent """
    
    def child_method(self): 
        """ Method specific to the Child class """
    pass
    """ This method does nothing for the moment """


child_instance = Child()
""" Creating an instance of the Child class """ 
print(dir(child_instance))
""" Displays all methods and attributes accessible for child_instance """
