class IntersectionIterator:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        #point to beginning of arrays
        self.p1 = 0
        self.p2 = 0

    def hasnext(self):
        if not self.l1 or not self.l2:
            return False
        if not self.inbounds():
            return False
        return True

    def next(self):
        if not self.hasnext():
            raise ValueError
        ans = self.l1[self.p1]
        self.p1+=1
        self.p2+=1
        self._update_ptrs()
        return ans

    def _update_ptrs(self):
        if not self.inbounds():
            return
        while self.l1[self.p1] != self.l2[self.p2]:
            if self.l1[self.p1] < self.l2[self.p2]:
                self.p1+=1
            else:
                self.p2+=1
            if not self.inbounds():
                return

    def inbounds(self):
        return self.p1 < len(self.l1) and self.p2 < len(self.l2)


ii = IntersectionIterator([1,2,3,4], [1,2,4])

print(ii.next(), ii.next(), ii.next())
