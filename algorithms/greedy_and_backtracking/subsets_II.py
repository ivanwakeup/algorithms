'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

intution:

this differs from subsets 1 because we might start buildign a path in our recursion that we've seen before. How do we keep track of if we've
seen it before?

we take advantage of the SORTED input and the order of DFS to stop early on paths we've seen before

tried to use a set originally, but this doesn't work because sets aren't ordered. actually.....if we first sort the path
and USE that as the set to check if we've seen it already, that might work.

'''


class Solution:
    def subsetsWithDup(self, nums):
        res = []
        seen = set()
        def dfs(nums, i, path, fs):
            if fs in seen:
                return
            seen.add(fs)
            res.append(path)
            if i >= len(nums):
                return
            for j in range(i, len(nums)):
                nxt = path + [nums[j]]
                dfs(nums, j + 1, nxt, frozenset([str(nxt)]))
        nums.sort()
        dfs(nums, 0, [], frozenset())
        return res


sol = Solution()

print(sol.subsetsWithDup([1,2,2]))