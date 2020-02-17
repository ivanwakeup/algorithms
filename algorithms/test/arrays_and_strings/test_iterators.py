from algorithms.arrays_and_strings.iterators import Iterator, IntersectionIterator

from unittest.case import TestCase


class IntersectionIteratorTest(TestCase):

    def test_normal(self):
        i1 = Iterator([1, 2, 4, 5, 6])
        i2 = Iterator([1,3,5])
        ii = IntersectionIterator(i1, i2)
        self.assertEqual(ii.next(), 1)

    def test_normal2(self):
        i1 = Iterator([3,3,4,4])
        i2 = Iterator([3,4,5])
        ii = IntersectionIterator(i1, i2)
        ii.next()
        self.assertEqual(ii.next(), 4)

    def test_some_empty(self):
        i1 = Iterator([])
        i2 = Iterator([3,4,5])
        ii = IntersectionIterator(i1, i2)
        ii.next()
        self.assertEqual(ii.next(), None)
