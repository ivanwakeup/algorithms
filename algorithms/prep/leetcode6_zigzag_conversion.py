class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        matrix = [[0 for _ in range(len(s))] for _ in range(numRows)]
        row = 0
        col = 0
        while s:
            s1, nrow, ncol = self.fill_down(s, row, col, matrix)
            s2, nrow, ncol = self.fill_diag(s1, nrow, ncol, matrix)
            s = s2

        result = []
        print(matrix)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]:
                    result.append(matrix[row][col])

        return "".join(result)

    def fill_down(self, s, row, col, matrix):
        while row < len(matrix) and s:
            print(s[0])
            matrix[row][col] = s[0]
            s = s[1:]
            row += 1
        return s, row - 2, col + 1

    def fill_diag(self, s, row, col, matrix):
        while row > 0 and s:
            matrix[row][col] = s[0]
            s = s[1:]
            row -= 1
            col += 1
        return s, row, col


sol = Solution()

sol.convert("PAYPALISHIRING", 3)