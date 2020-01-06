import unittest
from ..deque import MyDeque
from inspect import ismethod

class Tests(unittest.TestCase):

    q = MyDeque()

    def test_1(self):
        self.q.append(1)
        self.q.append(2)
        self.q.append(3)
        self.assertTrue(self.q.popleft()==1)
        self.assertTrue(self.q.popleft()==2)
        self.assertTrue(self.q.popleft()==3)
        self.q.__init__()

    def test_2(self):
        self.q.appendleft(4)
        self.q.appendleft(2)
        self.assertTrue(self.q.pop()==4)
        self.assertTrue(self.q.pop()==2)