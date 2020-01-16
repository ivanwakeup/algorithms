'''
the idea is actually pretty straightforward:

do a modified binary search.

if we check arr[low] <= arr[mid], we KNOW for certain the rotation must occur in the right half.

THEN, (assuming arr[low] <= arr[mid]) if we just check that our TARGET is between arr[low] and arr[mid], we know to update our HIGH for next round to be
high = mid -1

if our predicate (arr[low] <= arr[mid]) isn't true, then the rotation must be in the left half.

so we just check the opposite case (is our target between mid and high, if so, search there) and search the appropriate half accordingly
'''

'''
perform a regular binary search
but once we calculate mid, if its the target return
if not, check if the value is between mid and high -> search there
else search low


[6,7,1,2,3]
'''


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                if nums[mid] > nums[hi] >= target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if nums[mid] < nums[lo] <= target:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return -1


sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))