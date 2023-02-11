import random


import random


class ProduceChars:
    """generator class to produce random numbers in a given range"""
    def __init__(self, start, stop, range1):
        self.start = start
        self.stop = stop
        self.range1 = range1
    def __iter__(self):
        current = self.start
        while current < self.range1:
            yield random.randrange(self.start, self.stop)
            current += 1
