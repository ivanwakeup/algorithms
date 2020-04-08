'''
intuitions:

FOR EVERY email we encounter we need to union it with its pair. the real bulk of the work is here:

for email in acc[1:]:
    if email not in em_to_id:
        em_to_id[email] = i
        dsu.union(em_to_id[acc[1]], em_to_id[email])

in this code, we always union a newly added email to our em_to_id map to the FIRST one that appears in the account. This helps us ensure that our unioned sets don't eventually drift apart.

consider the case of David and his emails:

[
    ["David","David0@m.co","David1@m.co"],
    ["David","David3@m.co","David4@m.co"],
    ["David","David4@m.co","David5@m.co"],
    ["David","David2@m.co","David3@m.co"],
    ["David","David1@m.co","David2@m.co"]
]

notice that if we don't merge the first input array (David0@m.co and David1@m.co), our output will be wrong, David0@m.co will appear in its own set given that we never updated the parent pointers array.
'''

from collections import defaultdict
class DSU:
    def __init__(self, size):
        self.p = [x for x in range(size + 1)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution(object):
    def accountsMerge(self, accounts):
        dsu = DSU(len(accounts))
        em_to_id = {}
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email not in em_to_id:
                    em_to_id[email] = i
                dsu.union(em_to_id[acc[1]], em_to_id[email])

        ans = defaultdict(list)
        for key in em_to_id:
            ptr = dsu.find(em_to_id[key])
            ans[ptr].append(key)

        return [[accounts[i][0]] + sorted(v) for i, v in ans.items()]
sol = Solution()
data = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
print(
    sol.accountsMerge(data)
)
