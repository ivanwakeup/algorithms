# class Solution(object):
#     triangle = None
#
#     def minimumTotal(self, triangle):
#         """
#         :type triangle: List[List[int]]
#         :rtype: int
#         """
#         if not triangle:
#             return 0
#
#         self.triangle = triangle
#         return self.mps(0, 0, 0, {})
#
#     def mps(self, i, j, cur_sum, memo):
#         key = (i, j)
#
#         # we've hit the end of the triangle
#         if i >= len(self.triangle):
#             return cur_sum
#
#         if key in memo:
#             return memo[key]
#
#         path_sum = min(
#             self.mps(i + 1, j, cur_sum + self.triangle[i][j], memo),
#             self.mps(i + 1, j + 1, cur_sum + self.triangle[i][j], memo)
#         )
#
#         memo[key] = path_sum
#
#         return path_sum
#
#
# sol = Solution()
#
# print(sol.minimumTotal([
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]))


class Solution(object):
    triangle = None

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        self.triangle = triangle
        return self.mps(0, 0, 0, {})

    def mps(self, i, j, memo):
        key = (i, j)

        # we've hit the end of the triangle
        if i == len(self.triangle) - 1:
            return self.triangle[i][j]

        if key in memo:
            return memo[key]

        path_sum = self.triangle[i][j] + min(
            self.mps(i + 1, j, memo),
            self.mps(i + 1, j + 1 memo)
        )

        memo[key] = path_sum

        return path_sum


sol = Solution()

print(sol.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))