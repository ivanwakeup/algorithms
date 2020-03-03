'''
intuition here:

we use the partition scheme from quicksort to reduce our array search space by HALF on each recursive call. This leads
to an expected runtime of O(n)....the proof for this must be insane tho!

other approaches:
1. use a min-heap for kth largest or max-heap for kth smallest, once the heap is size K, pop the top element if the
next element in the input array is greater than it, continue until we've examined all elements of input

at the end, the top of the heap is clearly the answer if we have K elements in the heap.
'''
import random
class Solution:
    def findKthLargest(self, nums, k):
        #invert k so we're really looking for the kth smallest element instead of kth largest
        k = len(nums)-k

        def do_find(nums, lo, hi):
            if not nums:
                return 0
            piv = random.randint(lo, hi)
            idx = self.partition(nums, piv, lo, hi)
            if idx == k:
                return nums[idx]
            elif idx < k:
                return do_find(nums, idx+1, hi)
            else:
                return do_find(nums, lo, idx-1)

        return do_find(nums, 0, len(nums) - 1)

    def partition(self, nums, piv, lo, hi):
        nums[piv], nums[hi] = nums[hi], nums[piv]
        start = lo - 1
        for i in range(lo, hi):
            if nums[i] <= nums[hi]:
                start += 1
                nums[start], nums[i] = nums[i], nums[start]
        nums[hi], nums[start + 1] = nums[start + 1], nums[hi]
        return start + 1

sol = Solution()
data = [3,2,1,5,6,4,7]
k=2
print(
    sol.findKthLargest(data, k)
)