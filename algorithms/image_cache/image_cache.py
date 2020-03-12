import sys
import requests
from collections import OrderedDict


class LRUCache:

    def __init__(self, size):
        self.cache = OrderedDict()
        self.size = size

    def get(self, key):
        if key in self.cache:
            tmp = self.cache[key]
            del self.cache[key]
            self.cache[key] = tmp
            return self.cache[key]
        return None

    def set(self, key, value):
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






