'''
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26





seems like a straight up backtracking approach

observation:
if we create a concatenation that has non unique characters we can stop on that current search
how do we check?
    -pass a dict forward in the recursion
    -iterate over next word to consider, if anything matches return early

pseudocode:
    for i in arr:
        if arr[i] not in cur_set:
            dfs(cur_set+arr[i], i+i)

    on each level of update largest_len if cur_path is larger



OPTIMIZATIONS:
realizing that we can optimize the uniqueness check in a few ways,
instead of just checking set unions between the word and cur_set, iterate over the current word and add items to the cur_set
as they aren't there, and just return if they are.

make sure to create a copy of the set to pass down the recursion tree.

'''


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        res = {'ans': 0}

        def unique(word, cur_set):
            for char in word:
                if char in cur_set:
                    return False
                cur_set.add(char)
            return True

        def dfs(arr, i, cur_set):
            if len(cur_set) > res['ans']:
                res['ans'] = len(cur_set)
            if i >= len(arr):
                return
            for j in range(i, len(arr)):
                nxt = cur_set.copy()
                if unique(arr[j], nxt):
                    dfs(arr, j + 1, nxt)

        dfs(arr, 0, set())
        return res['ans']

