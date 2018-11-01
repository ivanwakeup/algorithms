'''
a linked list is a recursive data structure that contain nodes, each of which contain a reference to the next node in the list (and the previous for doubly linked lists
you can maintain a dummy node that points to the head for ease of operation
a dummy node that points to the tail also allows for constant time deletion of elements at the tail
'''
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node Value: {}".format(self.data)

class DoublyNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.dummy = Node(0)
        self.head = None
        self.dummy.next = self.head
        self.tail = self.head

    def __repr__(self):
        return self.print_ll()

    def reverse(self):
        #each node should point to the one before it
        prev = None
        cur = self.head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        self.head = prev


    def insertHead(self, node):
        tmp = self.head
        self.head = node
        node.next = tmp
        if not tmp:
            self.tail = self.head
        self.dummy.next = self.head

    def insertTail(self, node):
        tmp = self.tail
        if tmp:
            tmp.next = node
            self.tail = node
        else:
            self.insertHead(node)

    def search(self, val):
        cur = self.head
        while cur:
            if cur.data == val:
                print("Found Value! {} at {}".format(cur.data, id(cur)))
                return cur.data
            cur = cur.next
        print("Didn't find value {}".format(val))
        return -1

    def delete(self, val):
        prev = cur = self.head
        if cur.data == val:
            self.head = cur.next
            return
        while cur:
            if cur.data == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

    def print_ll(self):
        cur = self.head
        str = ""
        while cur:
            str += "{}->".format(cur.data)
            cur = cur.next
        str += "NIL"
        print(str)
        return(str)


ll = LinkedList()
ll.insertHead(Node(1))
ll.insertHead(Node(2))
ll.insertHead(Node(3))
ll.insertTail(Node(4))
ll.insertHead(Node(5))

ll.print_ll()

ll.search(3)
ll.search(-1)

ll.delete(1)

ll.reverse()
ll.print_ll()
ll.reverse()
ll.print_ll()


