import requests
from collections import OrderedDict


class LRUCache:

    def __init__(self, size):
        #use ordereddict for LRU cache to get near-constant time LRU lookups
        self.cache = OrderedDict()
        self.size = size
        self.used = 0

    def get(self, key):
        if key in self.cache:
            tmp = self.cache[key]
            del self.cache[key]
            self.cache[key] = tmp
            return self.cache[key]
        return None

    def set(self, key, value):
        self.size-=len(value)
        print(self.size)
        while self.size < 0 and len(self.cache) >= 1:
            print("cache size limit reached, evicting key...")
            lru = self.cache.popitem(last=False)
            self.size+=len(lru[1])
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        return


result = []

with open('images.txt') as f:
    byte_size = int(f.readline().strip())
    cache = LRUCache(byte_size)

    num_urls = int(f.readline().strip())
    for line in f.readlines():
        url = line.strip()
        cached = cache.get(url)
        if cached:
            result.append([url, "IN_CACHE", len(cached)])
        else:
            res = requests.get(url)
            #store literal bytes that makeup image
            bytes = list(res.content)
            cache.set(url, bytes)
            result.append([url, "DOWNLOADED", len(bytes)])

for item in result:
    print(" ".join([str(x) for x in item]))






