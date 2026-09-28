from queue import PriorityQueue
import time


class Cache:

    def __init__(self):
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        pass

    def evict(self):
        #implement eviction policy depending on the type of cache
        pass


class SimpleCache(Cache):

    def __init__(self, max_size=3, *args, **kwargs) -> None:
        self.cache = {}
        self.max_cache_size = max_size
        self.used_map = {}
        self.pq = PriorityQueue()

    def set(self, key, value):

        cur_time = time.monotonic()
        self.cache[key] = value
        self.used_map[key] = cur_time
        self.pq.put((cur_time, key, value))
        
        if len(self.cache) > self.max_cache_size:
            print("cache full, evicting oldest key..")
            self.evict_lru()


    def get(self, key):
        if key in self.cache:
            cur_time = time.monotonic()
            val = self.cache[key]
            self.used_map[key] = cur_time
            self.pq.put((cur_time, key, val))
            return val
        else:
            return None

    def evict(self):
        self.evict_lru()

    def evict_lru(self):

        time, key, value = self.pq.get()
        if time != self.used_map[key]:
            print(f"discarding stale key for {key} and {value}")
            self.evict_lru()
        else:
            print(f"deleting cached key for {key}")
            del self.cache[key]
            del self.used_map[key]

        

# c = SimpleCache()
# c.set(1, 2)
# c.set(2, 15)
# c.get(1)
# c.get(2)
# c.get(3)
# c.get(1)
# c.set(3, 2)
# c.set(4, 14)
# c.set(2, 10)
# print(c.get(1))
# print(c.cache)
        
from collections import OrderedDict

class BetterLRUCache(Cache):

    def __init__(self):
        super().__init__()
        self.cache = OrderedDict()
        self.max_size = 3

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.max_size:
                    self.evict()

    def _evict_lru(self):
        res = self.cache.popitem(last=False)
        print(self.cache)
        print(f"evicting latest key at {res}")

    def evict(self):
        self._evict_lru()

c = BetterLRUCache()
c.set(1, 2)
c.set(2, 15)
c.get(1)
c.get(2)
c.get(3)
c.get(1)
c.set(3, 2)
c.set(4, 14)
c.set(2, 10)
print(c.get(1))
print(c.cache)