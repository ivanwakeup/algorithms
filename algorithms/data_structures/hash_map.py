'''
implement a hash map

needs to:

add_key 0(1) expected, 0(n) worst case
delete_key
lookup_key


approach:
need to compute a hash for keys to be added
mod that hash value by



considerations:
when do we increase the size of the array storing the values?
we could do it every time the occupied space > half the total space

the probability of a hash collision is about 50% when the table is half full
'''


class LinkedNode:

    def __init__(self, val):
        self.data = val
        self.next = None

    def __repr__(self):
        return self.data

    def __eq__(self, other):
        return other == self.data


class LinkedHashSet:

    def __init__(self):
        self.size = 7
        self.table = [LinkedNode("*") for _ in range(self.size)]
        self.occupied = 0

    def add_key(self, key):
        if self.occupied >= self.size//2:
            self.add_size()
        bucket = hash(key)%self.size
        head = self.table[bucket]
        prev = LinkedNode("dummy")
        while head:
            if head == key:
                return
            prev = head
            head = head.next
        prev.next = LinkedNode(key)
        self.occupied+=1

    def add_size(self):
        self.size *= 2
        self.table = self.table + [LinkedNode("*") for _ in range(self.size)]


    def delete_key(self, key):
        bucket = hash(key) % self.size
        head = self.table[bucket]

        prev = head
        deleted = False
        while head:
            if head == key:
                tmp = head.next
                prev.next = tmp
                deleted = True
                break
            else:
                prev = head
                head = head.next
        if not deleted:
            raise ValueError("delete key doesn't exist")
        self.occupied-=1

    def key_exists(self, key):
        bucket = hash(key) % self.size
        head = self.table[bucket]
        while head:
            if head == key:
                return True
            else:
                head = head.next
        return False



hm = LinkedHashSet()
hm.add_key(1)
hm.delete_key(1)
print(hm.occupied)





