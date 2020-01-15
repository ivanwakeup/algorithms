'''
lets implement a deque.

it should support:
    1. popleft
    2. pop
    3. append
    4. appendleft



approach:
two arrays?

use statically sized arrays_and_strings, and start appending at the middle
keep pointers to determine where pops and pushes should happen:
    can we do it with just 2 pointers?


initialize two pointers to the same position, LP and RP:
appendleft - moves LP left
popleft - moves LP right
append - moves RP right
pop - moves RP left

if we run out of size on either the right or the left, add some size to that side

if we add size to the beginning of the arrays_and_strings, we need to update the lp pointer to where it belongs:
    1. cur_idx + size_added
    2.
'''

class MyDeque:

    def __init__(self):
        self.arr = [NoEntry] * 3
        self.lp = 0
        self.rp = 1

    def appendleft(self, item):
        if self.lp < 0:
            added = self.resize_left()
            self.lp += added
        self.lp -= 1
        self.arr[self.lp] = item

    def popleft(self):
        to_return = self.arr[self.lp] if self.arr[self.lp] != NoEntry else None
        self.arr[self.lp] = NoEntry
        self.lp -= 1
        return to_return

    def append(self, item):
        if self.rp >= len(self.arr)-1:
            self.resize()
        self.rp += 1
        self.arr[self.rp] = item

    def pop(self):
        to_return = self.arr[self.rp] if self.arr[self.rp] != NoEntry else None
        self.arr[self.rp] = NoEntry
        self.rp -= 1
        return to_return

    def resize_left(self):
        space_to_add = len(self.arr)//2
        self.arr = ([NoEntry] * space_to_add) + self.arr
        return space_to_add

    def resize(self):
        space_to_add = len(self.arr) // 2
        self.arr = self.arr + ([NoEntry] * space_to_add)
        return


class NoEntry:
    pass


'''
let's test the class
'''