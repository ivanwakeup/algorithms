'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?




a really cool approach to solving this problem is to:
effectively do an insertion sort partition in two passes

on the first pass, we just try and create a partition such that all the zeros are in the correct place
on the second pass, we start from the right side and create a partition such that all the twos are at the end

naturally, if we can put all the 0s at the start and all the zeros at the end, we'll be left with just the ones
in the middle.

'''


# class Solution:
#     def sortColors(self, nums):
#         piv = 1
#
#         i = -1
#         for j, n in enumerate(nums):
#             if n < piv:
#                 i+=1
#                 nums[j], nums[i] = nums[i], nums[j]
#         i = len(nums)
#         for j in range(len(nums)-1, -1, -1):
#             if nums[j] > piv:
#                 i-=1
#                 nums[j], nums[i] = nums[i], nums[j]
#
#
# sol = Solution()
# data = [2,0,0,1,1,2]
# sol.sortColors(data)
# print(data)



'''
we can make the solution better by creating the 3 necessary partitions in a single pass.

the more obvious way to do this would be to have to start a low pointer at zero and a high pointer at the end of the array

then we iterate through the array
    if the current value is LESS that the pivot, swap it with the lo pointer
    if its greater, swap it with the high pointer
    move appropriate pointers accordingly
    
we are done if our current pointer meets our high pointer
'''

class Solution:
    def sortColors(self, nums):
        lo = mid = 0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] < 1:
                nums[mid], nums[lo] = nums[lo], nums[mid]
                lo+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high-=1


sol = Solution()
data = [2,0,0,1,1,2]
sol.sortColors(data)
print(data)