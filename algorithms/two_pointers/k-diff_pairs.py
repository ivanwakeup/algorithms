'''
ex
[3,1,4,1,5] => [1,1,3,4,5], k = 2

[1,1,1,3,3,4,6]

[1,1,3,4,5]


[-3, 5, 7, -2, -4]

[1,1,3,4,5]

idea:
sort array, and use a sliding window approach
once we find a pair that is a result, move both lo and hi pointers
forward until they dont point to the same elements we created a result out of
'''


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        lo = 0
        hi = 1
        result = 0
        while lo < len(nums) and hi < len(nums):

            if abs(nums[hi] - nums[lo]) == k:
                result += 1
                lo += 1
                hi += 1

                while lo < len(nums) and nums[lo] == nums[lo - 1]:
                    lo += 1

                while hi < len(nums) and nums[hi] == nums[hi - 1]:
                    hi += 1

            elif abs(nums[hi] - nums[lo]) < k:
                hi += 1
            else:
                lo += 1

            if hi <= lo:
                hi = lo + 1

        return result



'''
there is a way simpler solution than using the sort/two-pointer approach here.

if we just use a counter to keep track of the number of elements, we just need to check
for each item if its complement exists in the counter. (does i+k exist?)

we could almost just use a set instead of a counter, but the counter helps with the case when k == 0,
we need to ensure there is at least 2 of a given number i => abs(i-i) == 0.
'''
class Solution:
    def findPairs_counter(self, nums, k):
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res