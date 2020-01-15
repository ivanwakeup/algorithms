'''
lets implement a queue with an arrays_and_strings.


[1,2,3,4,5] -> append on the left side, pop on the right?
we could initialize an empty arrays_and_strings and double it in size every time the queue grows.
[null, null, 1]
        ^
[3,2,1]
 ^

arrays_and_strings full, so add some slots
[null,null,null,3,2,1]
             ^
now pop() -> return 1, space becomes null

[null,null,null,3,2,null]
             ^     ^


as we pop from the right, how do we reclaim the arrays_and_strings slots that are now NULL?
keep track of the arrays_and_strings size, and let it be circular

keep a pop and a push pointer that says where to pop and push from, both move to the left

'''


class Queue:

    def __init__(self):
        self.arr = [NoEntry] * 2
        self.size = 0
        self.popptr = -1
        self.pushptr = -1

    def push(self, item):
        if self.size >= len(self.arr):
            self.resize()
        self.arr[self.pushptr] = item
        self.size += 1
        self.pushptr = self.calc_ptr_pos(self.pushptr)

    def pop(self):
        if not self.size:
            return None
        item = self.arr[self.popptr]
        self.popptr = self.calc_ptr_pos(self.popptr)
        self.size-=1
        return item

    def calc_ptr_pos(self, ptr):
        nxt = -1 + ptr
        return nxt % len(self.arr)

    def resize(self):
        self.arr = [NoEntry] * len(self.arr) + self.arr


class NoEntry:
    pass


q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(3)
q.push(2)
q.push(1)
print(q)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
