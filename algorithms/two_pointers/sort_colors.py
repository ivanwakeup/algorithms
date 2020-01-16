'''
counting sort solution:

create array that stores the count of each num at the correct index
create pointer for nums, and one for counts_array

while counts_array[pointer] > 0:
    add that index to current nums[pointer]
    move nums[pointer]
    counts_array[pointer]-=1
'''
class Solution:
    def sortColors(self, nums):
        counts = [0 for _ in range(3)]
        for num in nums:
            counts[num]+=1
        i = 0
        j = 0
        while i < len(nums):
            while counts[j] > 0:
                nums[i] = j
                counts[j]-=1
                i+=1
            j+=1