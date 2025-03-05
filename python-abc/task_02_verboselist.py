#!/usr/bin/env python3
"""
a class named VerboseList that extends the Python list class
"""


class VerboseList(list):
    """
    Override the append method
    """
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    """
    Override the extend method
    """
    def extend(self, iterable):
        items_added = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {items_added} items.")

    """
    Override the remove method
    """
    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    """
    Override the pop method
    """
    def pop(self, index=-1):
        item = self[index]  # Capture the item to be popped before removing it
        print(f"Popped {item} from the list.")
        return super().pop(index)
