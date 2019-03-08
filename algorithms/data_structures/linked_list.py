class KVDoubleNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class KVDoubleLinkedList:

    '''
    init double linked list with dummy head and tail nodes
    '''
    def __init__(self):
        self.head = KVDoubleNode("dummy", "dummy")
        self.tail = KVDoubleNode("dummy", "dummy")
        self.head.next = self.tail
        self.tail.prev = self.head

    '''
    adds a node to a this doubly linked chain of nodes.
    to add a node, we need to update the tail of p to point at the newly added node
    
    '''
    def add_node(self, node):
        cur = self.tail.prev
        cur.next = node
        node.prev = cur
        node.next = self.tail
        self.tail.prev = node


    def print_ll(self):
        print_arr = []
        start = self.head
        while start:
            if start.next:
                print_arr.append("({}, {})".format(start.key, start.val))
                print_arr.append("<--->")
            else:
                print_arr.append("({}, {})".format(start.key, start.val))
            start = start.next
        print("".join(print_arr))


ll = KVDoubleLinkedList()
ll.add_node(KVDoubleNode(1,1))
ll.add_node(KVDoubleNode(2,2))

ll.print_ll()


