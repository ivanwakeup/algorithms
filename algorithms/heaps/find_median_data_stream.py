'''
approaches:
keep an array in sorted order, insert each new element in sorted order. addNum costs O(nlogn)


intuition:
MAX_HEAP stores everything less than the median
MIN_HEAP stores everything greater than the median

if next element is < median put it on MAX_HEAP else MIN_HEAP
perform balance_heap() procedure
perform calc_median() procedure
[1,2,3,4] -> when we
'''
from queue import PriorityQueue


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.median = float('inf')
        self.maxh = PriorityQueue()
        self.minh = PriorityQueue()

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.median:
            self.maxh.put(-num)
        else:
            self.minh.put(num)
        self._balance()
        self._calc_median()

    def findMedian(self):
        """
        :rtype: float
        """
        return self.median

    def _balance(self):
        if abs(self.maxh.qsize() - self.minh.qsize()) <= 1:
            return
        if self.maxh.qsize() > self.minh.qsize():
            item = self.maxh.get()
            self.minh.put(-item)
        else:
            item = self.minh.get()
            self.maxh.put(-item)

    def _calc_median(self):
        if self.maxh.qsize() == self.minh.qsize():
            self.median = (float(-self.maxh.queue[0]) + float(self.minh.queue[0])) // 2
        elif self.maxh.qsize() > self.minh.qsize():
            self.median = -self.maxh.queue[0]
        else:
            self.median = self.minh.queue[0]

finder = MedianFinder()
finder.addNum(1)
finder.addNum(2)
print(finder.findMedian())