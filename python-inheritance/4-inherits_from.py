#!/usr/bin/python3

def is_instance_of_inherited_class(obj, cls):
    """
    Check if the object is an instance of a class that inherited directly or indirectly from the specified class.

    Parameters:
    obj (object): The object to check.
    cls (type): The class to check against.

    Returns:
    bool: True if obj is an instance of a class that inherited from cls, False otherwise.
    """
    return isinstance(obj, cls) and type(obj) is not cls


class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

dog = Dog()

print(is_instance_of_inherited_class(dog, Animal))  # True
print(is_instance_of_inherited_class(dog, Mammal))  # True
print(is_instance_of_inherited_class(dog, Dog))     # False
