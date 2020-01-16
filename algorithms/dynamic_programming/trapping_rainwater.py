'''
3 passes, store max_index
'''


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left = [0 for _ in range(len(height))]
        max_right = [0 for _ in range(len(height))]

        for i in range(1, len(height)):
            max_left[i] = max(height[i - 1], max_left[i - 1])

        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(height[i + 1], max_right[i + 1])

        area = 0

        for i in range(len(height)):
            area += max(0, min(max_left[i], max_right[i]) - height[i])

        return area