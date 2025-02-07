#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
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
