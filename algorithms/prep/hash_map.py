'''
implement a hash map with an arrays_and_strings
need hashing function? takes key that and stores the value at the position in arrays_and_strings computed by the hash function
stores
'''
class HashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def get(self, key):
        position = self.__compute_hash(key)
        try:
            value = self.values[position]
            return value
        except Exception:
            print("no value with this key!!")
            raise Exception

    def put(self, key, value):
        pass

    def delete(self, key):
        pass

    '''
    good hash function should result in few collisions
    
    '''
    def __compute_hash(self, key):
        return bin(key) % len(self.values)