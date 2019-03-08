'''
an LRU (least recently used) stores items until it is full, at which point it discards
the least recently used item.

if PUT is called and the cache is full, we discard the least recently used item and insert the new item.
we'll also need to update which item has been least recently used?


the tricky part is how do we keep track of the items and what time they were used, while supporting both
PUT and GET operations in constant time?

'''


class LRUCache:

    def __init__(self):
        self.hm = {}
        self.used_queue = []

    def get(self, key):
        if key in self.hm:
            return self.hm[key]
        else:
            return -1

    def set(self, key, value):
        self.hm[key] = value


cache = LRUCache()

cache.set(1, 10)
print(cache.get(1))