class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.cur_min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x < self.cur_min:
            self.cur_min = x
        self.stack.append((x, self.cur_min))

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()

        if self.stack:
            self.cur_min = self.stack[-1][1]
        else:
            self.cur_min = float('inf')

    def getMin(self):
        """
        :rtype: int
        """
        return self.cur_min


class LinkedListStack:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, value):
        if not self.head:
            self.head = self.Node(value)
        else:
            new_node = self.Node(value)
            prev = self.head
            self.head = new_node
            self.head.next = prev

    def pop(self):
        if not self.head:
            raise ValueError("stack is empty!!")
        result = self.head.val
        nxt = self.head.next
        self.head = nxt
        return result


stack = LinkedListStack()
stack.push(-1)
stack.push(-2)
stack.push(3000)
stack.pop()
print(stack.pop())
stack.push(4)
stack.push(5)
stack.pop()
print(stack.pop())