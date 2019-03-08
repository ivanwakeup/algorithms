'''
an LRU (least recently used) stores items until it is full, at which point it discards
the least recently used item.

if PUT is called and the cache is full, we discard the least recently used item and insert the new item.
we'll also need to update which item has been least recently used?


the tricky part is how do we keep track of the items and what time they were used, while supporting both
PUT and GET operations in constant time?

'''


class LRUCache:

    def __init__(self, size):
        self.hm = {}
        self.used = {}
        self.space = size
        self.time = 0

    '''
    when we call this, we'll need to update the time at which the item we accessed was used, if it exists.
    '''
    def get(self, key):
        if key in self.hm:
            self.update_time(key)
            return self.hm[key]
        else:
            return -1

    def set(self, key, value):
        if key in self.hm:
            self.hm[key] = value
            self.update_time(key)
            return
        if self.space <= 0:
            lru = float('inf')
            delkey = None
            #should be able to do this part in constant time
            for ukey in self.used.keys():
                if self.used[ukey] < lru:
                    lru = self.used[ukey]
                    delkey = ukey
            #end part
            if delkey:
                del self.hm[delkey]
                del self.used[delkey]
            self.space+=1
            self.set(key, value)
        else:
            self.hm[key] = value
            self.used[key] = self.time
            self.space -= 1
            self.time += 1

    def update_time(self, key):
        if key in self.used:
            self.used[key] = self.time
            self.time +=1



cache = LRUCache(2)

cache.set(2, 1)
cache.set(1, 1)
cache.set(2,3)
cache.set(4,1)
print(cache.get(1))
print(cache.get(2))
