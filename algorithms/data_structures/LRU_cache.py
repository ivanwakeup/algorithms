'''
an LRU (least recently used) stores items until it is full, at which point it discards
the least recently used item.

if PUT is called and the cache is full, we discard the least recently used item and insert the new item.
we'll also need to update which item has been least recently used?


the tricky part is how do we keep track of the items and what time they were used, while supporting both
PUT and GET operations in constant time?

'''


class LRUCache1:

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


#
# cache = LRUCache1(2)
#
# cache.set(2, 1)
# cache.set(1, 1)
# cache.set(2,3)
# cache.set(4,1)
# print(cache.get(1))
# print(cache.get(2))



'''

'''
from algorithms.data_structures.linked_list import KVDoubleLinkedList, KVDoubleNode
class LRUCacheDoubleLinked:


    def __init__(self, size):
        #hm maps keys to KvDoubleNode objects
        self.hm = {}
        self.ll = KVDoubleLinkedList()
        self.size = size

    '''
    we are now using the linkedlist to keep track of when keys instead of incrementing a time variable
    and iterating over an arrays_and_strings to find the least used key when we need to evict it
    
    when we get a key, let's remove it from the linked list by manually deleting that node, and then append it to the end
    '''
    def get(self, key):
        if key not in self.hm:
            return -1
        node = self.hm[key]
        self.ll.delete_node(node)
        self.ll.add_node(node)
        return node.val

    '''
    here, if we're setting a key we first want to remove it from the hashmap and linkedlist if it exists already,
    and then re-add it to the end of the ll.
    
    if the key doesn't exist but our capacity is full, we want to just remove the node at the head of our linkedlist
    '''
    def set(self, key, value):
        if key in self.hm:
            existing_node = self.hm[key]
            self.ll.delete_node(existing_node)
            del self.hm[key]

        elif len(self.hm) >= self.size:
            to_del = self.ll.head.next
            self.ll.delete_node(to_del)
            del self.hm[to_del.key]

        node = KVDoubleNode(key, value)
        self.ll.add_node(node)
        self.hm[key] = node


lru = LRUCacheDoubleLinked(2)
lru.set(1,1)
lru.set(2,2)
lru.get(1)
lru.set(3,3)
print(lru.get(2))

