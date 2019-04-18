class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __eq__(self, other):
        return self.val == other


'''
plan:

use a hashmap that stores a string key : Node value


we want to:
add_key -> add it if size allows, otherwise evict LRU key then add
get_key -> get key if it exists and update LRU

'''
class DoubleLinkedList:

    def __init__(self):
        self.head = Node('dummy')
        self.cur = self.head

    def add_node(self, node):
        node.prev = self.cur
        self.cur.next = node
        self.cur = node
    '''
    3 cases:
    if node is in middle:
    just update prev.next = NODE.next
    node.next.prev = prev
    '''
    def delete_node(self, node):
        p = node.prev
        p.next = node.next
        #assumes the next node exists
        if node.next:
            node.next.prev = p

    def pop(self):
        n = self.head.next
        self.delete_node(n)
        return n

    def print_ll(self):
        print_arr = []
        start = self.head
        while start:
            if start.next:
                print_arr.append("{}".format(start.val))
                print_arr.append("<--->")
            else:
                print_arr.append("{}".format(start.val))
            start = start.next
        print("".join(print_arr))

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
#
# ll = DoubleLinkedList()
# ll.add_node(n1)
# ll.add_node(n2)
# ll.add_node(n3)
# ll.delete_node(n3)
# ll.print_ll()


'''
what does this help me do?

it helps me LOCATE a key to delete in constant time, instead of searching an entire linkedlist to find it
'''

class LinkedHashMap:

    def __init__(self, size):
        self.hm = {}
        self.size = size
        self.ll = DoubleLinkedList()

    def add_key(self, key):
        if key not in self.hm:
            if len(self.hm) >= self.size:
                n = self.ll.pop()
                del self.hm[n.val]
            to_add = Node(key)
            self.hm[key] = to_add
            self.ll.add_node(to_add)

    def get_key(self, key):
        if key not in self.hm:
            raise ValueError("key not present in {}".format(self))
        #its here, so we need to delete where its currently at and add it to the end
        n = self.hm[key]
        self.ll.delete_node(n)
        self.ll.add_node(n)
        return n.val


lhm = LinkedHashMap(2)
lhm.add_key(1)
lhm.add_key(2)
lhm.get_key(1)
lhm.add_key(3)
print(lhm.hm.keys())