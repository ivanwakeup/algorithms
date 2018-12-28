class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main_q = []
        self.tmp_q = []
        self.top = float('inf')

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.main_q.append(x)
        self.top = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.main_q) == 1:
            return self.main_q.pop(0)

        while len(self.main_q) > 1:
            if len(self.main_q) == 2:
                next_top = self.main_q.pop(0)
                self.top = next_top
                self.tmp_q.append(next_top)
                break

            self.tmp_q.append(self.main_q.pop(0))

        tmp = self.main_q.pop(0)

        self.main_q = self.tmp_q

        self.tmp_q = []

        return tmp

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.main_q

obj = MyStack()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()