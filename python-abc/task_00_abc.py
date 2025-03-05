#!/usr/bin/env python3
"""
an abstract class named Animal using the ABC package.
"""


from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses
        """
        pass


class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def sound(self):
        return "bark"


class Cat(Animal):
    def sound(self):
        return "meow"
