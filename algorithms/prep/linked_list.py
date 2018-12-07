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
        return "Address {} and Node Value: {}".format(id(self), self.data)


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

    def swapPairs(self):
        dummy = p = Node(0)
        head = self.head
        dummy.next = head
        while head and head.next:
            self.print_ll()
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            p.next = tmp
            head = head.next
            p = tmp.next
        self.head = dummy.next


# ll = LinkedList()
# ll.insertHead(Node(4))
# ll.insertHead(Node(3))
# ll.insertHead(Node(2))
# ll.insertHead(Node(1))
#
# ll.swapPairs()
#
# ll.print_ll()
#
# ll.search(3)
# ll.search(-1)
#
# ll.delete(1)
#
# ll.reverse()
# ll.print_ll()
# ll.reverse()
# ll.print_ll()


# def mergeTwoLists(l1, l2):
#     dummy = curr = Node(0)
#     while l1 and l2:
#         if l1.data < l2.data:
#             curr.next = l1
#             l1 = l1.next
#         else:
#             curr.next = l2
#             l2 = l2.next
#         curr = curr.next
#     curr.next = l1 or l2
#     return dummy.next
#
#
# l1 = Node(1)
# l1.next = Node(1)
# l1.next.next = Node(2)
#
# l2 = Node(2)
# l2.next = Node(3)
#
#
# out = mergeTwoLists(l1, l2)


def reverseKGroup(head, k):
    dummy = jump = Node(0)
    dummy.next = l = r = head
    while True:
        count = 0
        # only want to reverse the list if we still have list remaining once we get to k
        while r and count < k:
            r = r.next
            count += 1
        if count == k:
            # does this cur, pre assignment work?
            cur, pre = l, r
            # now l is at head, r is at end of reversal range
            for _ in range(k):
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            jump.next = pre
            jump = l
            l = r
        else:
            return dummy.next

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(3)
l1.next.next.next = Node(4)
l1.next.next.next.next = Node(5)



print(reverseKGroup(l1, 2))


