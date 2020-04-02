class UnionFindRedundantConnection:

    def __init__(self, n, edges):
        self.sets = [x for x in range(n+1)]
        self.union_edges(edges)

    def union_edges(self, edges):
        for e1, e2 in edges:
            res = self.union(e1, e2)
            if not res:
                print(f"found cycle at {e1}<->{e2}")

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return 0
        self.sets[p1] = p1
        self.sets[p2] = p1
        return 1

    def find(self, v):
        if v == self.sets[v]:
            return v
        curr = v
        while curr != self.sets[curr]:
            curr = self.sets[curr]
        return curr



edges = [[1,5],[3,4],[3,5],[4,5],[2,4]]
uf = UnionFindRedundantConnection(len(edges), edges)
