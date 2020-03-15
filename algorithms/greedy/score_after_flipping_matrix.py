'''
we know we can maximize each row by ensuring the first column is 1

then, we can jsut try to maximize each column
'''

from typing import List

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:

        for i, row in enumerate(A):
            if row[0] == 0:
                A[i] = [x ^ 1 for x in row]

        for col in range(1, len(A[0])):
            total = 0
            for row in range(0, len(A)):
                if row == 0:
                    continue
                else:
                    total += A[row][col]
            if total <= 1:
                for row in range(0, len(A)):
                    A[row][col] ^= 1

        result = 0
        for row in A:
            result += self.get_bin_int(row)

        print(A)
        return result

    def get_bin_int(self, bin_arr):
        bin_arr = [str(x) for x in bin_arr]
        res = "".join(bin_arr)
        return int(res, 2)


'''
[[1, 1, 0, 0], 
 [1, 0, 1, 0], 
 [1, 1, 0, 0]]




[[1, 0, 1, 1], 
 [1, 1, 0, 1], 
 [1, 0, 1, 1]]
'''
sol = Solution()
