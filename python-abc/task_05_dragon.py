#!/usr/bin/env python3

"""
Mixin class for swimming ability
"""
class SwimMixin:
    def swim(self):
        print("The creature swims!")

"""
Mixin class for flying ability
"""
class FlyMixin:
    def fly(self):
        print("The creature flies!")

"""
Dragon class inheriting from both mixins
"""
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")