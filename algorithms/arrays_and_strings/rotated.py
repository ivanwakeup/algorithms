def rotate(nums, k):
    for i in range(k):
        new_nums = [nums[-1]] + nums[:-1]
        nums = new_nums


print(rotate([1,2,3,4,5,6,7], 3))





'''
a routine to remember:

we can rotate an array by K steps by just:
reversing the array
then reversing the first K elements
then reversing the remaining k: len(arr) elements

its like magic, but the shit works.
'''
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        self.rev(nums, 0, len(nums)-1)
        self.rev(nums, 0, k-1)
        self.rev(nums, k, len(nums)-1)

    def rev(self, nums, lo, hi):
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo+=1
            hi-=1