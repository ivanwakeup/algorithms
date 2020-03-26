'''
examples:
[1,4,6] [3,3,4,5,6,10]

formula for how to partition the larger array?
len(small) + len(large) + 1/2 - SMALL_MID

why is this the formula?
think of it like finding the MID of the concatenated version of both arrays,
and offseting the partition point by wherever the partition point in the smaller array is

for example, if the part_idx in the smaller array = 0,
part_idx_larger is just the mid of the concatenated array

if its 1, then offset the partition point to the left by 1.

using the SMALL_MID to offset the partition point keeps the two halves LEFT and RIGHT of each input array
equivalent in size
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        small = nums1 if len(nums1) <= len(nums2) else nums2
        large = nums1 if len(nums1) > len(nums2) else nums2

        lo, hi = 0, len(small)
        while lo <= hi:
            small_mid = (hi + lo) // 2
            large_mid = (len(small) + len(large) + 1) // 2 - small_mid

            if small_mid < len(small) and large[large_mid - 1] > small[small_mid]:
                lo = small_mid + 1
            elif small_mid > 0 and small[small_mid - 1] > large[large_mid]:
                hi = small_mid - 1
            else:
                if not small_mid:
                    max_left = large[large_mid - 1]
                elif not large_mid:
                    max_left = small[small_mid - 1]
                else:
                    max_left = max(small[small_mid - 1], large[large_mid - 1])

                if (len(small) + len(large)) % 2:
                    return max_left

                if small_mid == len(small):
                    min_right = large[large_mid]
                elif large_mid == len(large):
                    min_right = small[small_mid]
                else:
                    min_right = min(small[small_mid], large[large_mid])

                return (max_left + min_right) / 2


sol = Solution()

d1 = [1,4,5,6,8]
d2 = [3,3,4]

print(
    sol.findMedianSortedArrays(d1, d2)
)