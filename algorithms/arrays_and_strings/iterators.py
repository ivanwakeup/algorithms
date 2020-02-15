class Iterator:
    def __init__(self, l):
        self.l = l
        self.ptr = 0

    def hasnext(self):
        if self.ptr < len(self.l):
            return True
        return False

    def next(self):
        if self.hasnext():
            ans = self.l[self.ptr]
            self.ptr+=1
            return ans
        raise ValueError


class IntersectionIterator:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        self.res = self._getnext()

    def hasnext(self):
        if not self.res:
            return False
        return True

    def next(self):
        ans = self.res
        self.res = self._getnext()
        return ans

    def _getnext(self):
        try:
            i1 = self.l1.next()
            i2 = self.l2.next()
        except ValueError:
            return None

        while i1 != i2:
            try:
                if i1 < i2:
                    i1 = self.l1.next()
                else:
                    i2 = self.l2.next()
            except ValueError:
                return None
        return i1


it1 = Iterator([1,2,4,5,6])
it2 = Iterator([1,3,5])

ii = IntersectionIterator(it1, it2)

print(ii.next(), ii.next(), ii.next())
