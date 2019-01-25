
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
        self.map_size = 7
        self.keys_stored = 0

        self.map = [self.Chain(None)] * self.map_size

    '''
    how do you compute a hash function?
    i want to take the "hash" value of whatever i supply and mod that by the size of the map to get the correct slot
    how should we handle increasing the table size?
    '''
    def hash(self, value):
        pass

    '''
    let's double the table size each time we need to resize
    to calculate primes, you only need to check
    '''
    @staticmethod
    def get_next_prime(cur):
        nxt = cur*2
        checker = 2
        while checker < nxt:
            if not nxt % checker:
                nxt -= 1
                checker = 2
                continue
            else:
                checker +=1
        return nxt


print(ChainedHashMap.get_next_prime(37))






