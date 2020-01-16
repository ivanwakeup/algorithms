class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j = 0,len(height)-1
        left_max = right_max = 0
        ans = 0
        while i<j:
            left_max = max(left_max,height[i])
            right_max = max(right_max,height[j])
            if left_max <= right_max:
                ans += (left_max-height[i])
                i += 1
            else:
                ans += (right_max-height[j])
                j -= 1
        return ans