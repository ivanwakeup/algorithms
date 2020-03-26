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

            maxSmallLeft = small[small_mid - 1] if small_mid > 0 else float('-inf')
            minSmallRight = small[small_mid] if small_mid < len(small) else float('inf')

            maxLargeLeft = large[large_mid - 1] if large_mid > 0 else float('-inf')
            minLargeRight = large[large_mid] if large_mid < len(large) else float('inf')

            if maxSmallLeft > minLargeRight:
                hi = small_mid - 1
            elif maxLargeLeft > minSmallRight:
                lo = small_mid + 1
            else:
                if not (len(small) + len(large)) % 2:
                    return (max(maxSmallLeft, maxLargeLeft) + min(minSmallRight, minLargeRight)) / 2
                else:
                    return max(maxSmallLeft, maxLargeLeft)


sol = Solution()

d1 = [1,4,5,6,8]
d2 = [3,3,4]

print(
    sol.findMedianSortedArrays(d1, d2)
)