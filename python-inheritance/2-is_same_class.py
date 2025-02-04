#!/usr/bin/python3

def is_exact_instance(obj, cls):
    return type(obj) is cls


class MyClass:
    pass

class AnotherClass:
    pass

obj1 = MyClass()
obj2 = AnotherClass()


print(is_exact_instance(obj1, MyClass))  # Output: True
print(is_exact_instance(obj2, MyClass))  # Output: False
print(is_exact_instance(obj1, AnotherClass))  # Output: False
