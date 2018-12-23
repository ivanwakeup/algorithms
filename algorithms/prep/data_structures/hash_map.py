
'''
need a hashing function to compute bucket within array
how should hash collisions be resolved?

questions:
1. how do i know how big of an array i need?
'''
class ChainedHashMap:

    class Chain:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.map_size = 8

        self.map = [self.Chain(None)] * self.map_size


    def hash(self, value):
        pass

