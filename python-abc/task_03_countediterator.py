#!/usr/bin/env python3
"""
class named CountedIterator that extends the built-in iterator
obtained from the iter function
"""


class CountedIterator:
    def __init__(self, iterable):
        """
        Initialize the iterator and the counter
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """
        Fetch the next item from the iterator
        """
        try:
            item = next(self.iterator)
            """
            Increment the counter
            """
            self.counter += 1
            return item
        except StopIteration:
            """
            Raise StopIteration when no items are left
            """
            raise StopIteration

    def get_count(self):
        """
        Return the current counter value
        """
        return self.counter
