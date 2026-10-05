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
        print(f"evicting oldest key at {res}")

    def evict(self):
        self._evict_lru()

# c = BetterLRUCache()
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



class ListNode:

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class MyOrderedDict():

    def __init__(self) -> None:
        self.hm = {}
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_end(self, key):
        if key not in self.hm:
            return
        node = self.hm[key]
        self._remove_node(node)
        self._insert_node(node)

    def set(self, key, value):
        if key in self.hm:
            self._remove_node(self.hm[key])
        item = ListNode(key, value)
        self.hm[key] = item
        self._insert_node(item)

    def get(self, key):
        if key in self.hm:
            return self.hm[key].value
        return None

    def popfirst(self):
        if not self.hm:
            return None
        node = self.head.next
        del self.hm[node.key]
        self._remove_node(node)
        return node.value
    
    def _remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _insert_node(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node


from collections import defaultdict

from dataclasses import dataclass

@dataclass
class CacheItem:
    key: str
    val: str
    frequency: int = 1

from typing import Generic, TypeVar

K = TypeVar("K")

class GenericListNode(Generic[K]):

    def __init__(self, value: K) -> None:
        self.value = value
        self.prev = None
        self.next = None

class LFUDoublyLinkedListContainer:

    def __init__(self) -> None:
        self.head = GenericListNode(None)
        self.tail = GenericListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self._len = 0

    def __len__(self):
        return self._len

    def remove_node(self, node):
        if node.next and node.prev:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
            self._len-=1

    def insert_node(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self._len+=1

    def popfirst(self):
        node = self.head.next
        self.remove_node(node)
        return node

    
class SimpleLFUCache(Cache):

    def __init__(self, cache_size=3):
        super().__init__()
        self.hm = {}
        self.counts = defaultdict(LFUDoublyLinkedListContainer)
        self.cache_size = cache_size
        self.min_freq = 1

    def set(self, key, val):
        if key not in self.hm:
            item = CacheItem(key, val, 1)
            node = GenericListNode[CacheItem](item)
            self.hm[key] = node
            self.counts[1].insert_node(node)
            self.min_freq = 1
        else:
            node = self.hm[key]
            freq = node.value.frequency
            self.counts[freq].remove_node(node)
            if len(self.counts[freq]) == 0 and freq == self.min_freq:
                self.min_freq+=1
            node.value.frequency+=1
            node.value.val = val
            self.counts[node.value.frequency].insert_node(node)

        if len(self.hm) > self.cache_size:
            self.evict()

    def get(self, key):
        if key not in self.hm:
            return None
        item = self.hm[key]
        self.counts[item.value.frequency].remove_node(item)
        if len(self.counts[item.value.frequency]) == 0 and item.value.frequency == self.min_freq:
            self.min_freq+=1
        item.value.frequency+=1
        self.counts[item.value.frequency].insert_node(item)
        return item.value.val
        
    def evict(self):
        res = self.counts[self.min_freq].popfirst()
        if len(self.counts[self.min_freq]) == 0:
            self.min_freq+=1
        del self.hm[res.value.key]


import threading

@dataclass
class TTLCacheItem:
    key: str
    val: str
    expired_at: float

class TTLCache(Cache):

    def __init__(self, cache_size=3, ttl_seconds=10, eviction_thread=False):
        self.hm = OrderedDict()
        self.cache_size = cache_size
        self.ttl_seconds = ttl_seconds
        self._TIME_ADD_NS = self.ttl_seconds * 1_000_000_000
        self._lock = threading.Lock()

        #spawn cleaup daemon
        def background_eviction_loop():
            while True:
                self.cleanup()
                time.sleep(10)

        if eviction_thread:
            d = threading.Thread(target=background_eviction_loop, daemon=True)
            d.start()

    
    def get(self, key):
        with self._lock:
            if key in self.hm:
                if self._is_expired(self.hm[key]):
                    del self.hm[key]
                    return None
                else:
                    return self.hm[key].val
            return None

    def put(self, key, value):
        with self._lock:
            new_item = TTLCacheItem(key, value, time.monotonic_ns() + self._TIME_ADD_NS)
            if key in self.hm:
                self.hm.move_to_end(key)
            self.hm[key] = new_item
            if len(self.hm) > self.cache_size:
                self._evict()

    def cleanup(self):
        with self._lock:
            self._ttl_evict()


    def _evict(self):
        self._ttl_evict()
        if len(self.hm) > self.cache_size:
            self._evict_oldest()
    

    def _ttl_evict(self):
        while self.hm and self._is_expired(self.hm[next(iter(self.hm))]):
            self.hm.popitem(last=False)

    def _evict_oldest(self):
        self.hm.popitem(last=False)

    def _is_expired(self, item):
        return item.expired_at < time.monotonic_ns()

    






            

        




        