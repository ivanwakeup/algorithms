'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]



'''


'''
here's an incorrect solution. it's close, but the problem is that because the set is mutable, once we add an item we've "used"
to the set, we have no way to remember what level of recursion that was used in--and it negatively affects other levels of recursion.

this code will essentially try and build a solution set one number at a time monotonically, and if it can't--everything just fails
because the recursion will bubble back up to the first failure and ultimately add every candidate number to the same mutable set.

in other words, it doesn't PROPERLY backtrack to the point of where our solution failed and remove any elements that caused the backtrack to fail!


example:
this code works for input k=3, n=6, because it'll hit it a solution set on its first root->leaf DFS.
'''
class Solution:
    def combinationSum3_INCORRECT(self, k, n):
        res = []

        used = set()

        def dfs(cur_sum, path):
            if len(path) == k:
                if cur_sum == n:
                    res.append(path)
                return

            if len(path) < k:
                for i in range(1, 10):
                    if i in used:
                        continue
                    used.add(i)
                    dfs(cur_sum + i, path + [i])

        dfs(0, [])
        return res



'''
the correct solution is to pass the candidate set of numbers that are still possible to use FORWARD in the recursion.


because this is COMBINATIONS we're looking for (order of the solution set doesn't matter), we need to completely remove a number
once we've started considering it in a solution set.

there is a subtle difference between this:
'''
class Solution:
    def combinationSum3(self, k, n):
        res = []

        def dfs(cur_sum, path, candidates):
            if len(path) == k:
                if cur_sum == n:
                    res.append(path)
                return

            if len(path) < k:
                for i in candidates:
                    #doesn't work, because we only remove the CURRENT index from the candidates, instead
                    #of the current index and everything else before it that we've already considered.
                    dfs(cur_sum + i, path + [i], candidates.difference({i}))

        dfs(0, [], set(range(1, 10)))
        return res



'''
THIS is correct
'''
class Solution:
    def combinationSum3(self, k, n):
        res = []

        def dfs(cur_sum, path, candidates):
            if len(path) == k:
                if cur_sum == n:
                    res.append(path)
                return

            if len(path) < k:
                #create a copy of the candidates
                cur = candidates.copy()
                for i in candidates:
                    #and keep track of what we're currently considering as well as everything we considered previously!
                    cur.remove(i)
                    dfs(cur_sum + i, path + [i], cur)

        dfs(0, [], set(range(1, 10)))
        return res