'''
learnings from implementing this again:

1. we position nodes to delete at the tail, by always pushing the LRU node to the HEAD
2. initalize the double linked list with a head and a tail to make insertions and deletions easy
3. when we PUT a new key, val we check to see if that key exists in the cache already, and just evict it if it does, then re-put it
4. storing the KEY and VAL in the node itself makes deletions from the hashmap when we only have a node reference easier.
'''
class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.val)

class LRUCache:


    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node("#", 'head')
        self.tail = Node("#", 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hm = {}

    def get(self, key: int) -> int:
        if key in self.hm:
            self._do_put(self.hm[key])
            return self.hm[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self._evict(self.hm[key])
        if not self.cap:
            self._evict(self.tail.prev)
        node = Node(key, value)
        self._do_put(node)
        self.hm[key] = node
        self.cap-=1

    def _delete(self, node):
        p = node.prev
        nxt = node.next
        p.next = nxt
        nxt.prev = p

    def _evict(self, node):
        del self.hm[node.key]
        self._delete(node)
        self.cap+=1

    def _do_put(self, node):
        if node.prev and node.next:
            self._delete(node)
        after = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next = after
        after.prev = node








cache = LRUCache(1)

cache.put(2,1)
print(
    cache.get(2)
)
cache.put(3, 2)
print(
    cache.get(2)
)

