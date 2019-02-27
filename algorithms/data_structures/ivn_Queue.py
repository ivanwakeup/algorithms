class LinkedListQueue:

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        self.cur = None

    #you need the self.cur pointer (aka the "tail" pointer)
    def enqueue(self, value):
        if not self.head:
            self.head = self.Node(value)
            self.cur = self.head
        else:
            #when you set cur.next, head.next also is updated! this is because CUR itself is reference, but when you use self.cur.next you're actually assigning the NEXT pointer from the physical object in memory
            self.cur.next = self.Node(value)
            self.cur = self.cur.next

    def dequeue(self):
        if not self.head:
            raise ValueError("nope!! its not here")
        result = self.head.val
        new_head = self.head.next
        self.head = new_head
        return result


queue = LinkedListQueue()
queue.enqueue(-1)
queue.enqueue(-2)
queue.enqueue(3000)
queue.enqueue(4)
queue.enqueue(5)


while queue.head:
    print(queue.dequeue())

