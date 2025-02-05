#!/usr/bin/python3
def is_instance_of(obj, cls):
    return isinstance(obj, cls)


class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(is_instance_of(dog, Animal))  # True
print(is_instance_of(cat, Animal))  # True
print(is_instance_of(dog, Cat))     # False
