'''
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for row in range(0, n // 2):
        for col in range(row, n - row - 1):
            tmp = matrix[row][col]

            # swap left to top
            matrix[row][col] = matrix[n - col - 1][row]

            # swap bottom to left
            matrix[n - col - 1][row] = matrix[n - row - 1][n - col - 1]

            # swap right to bottom
            matrix[n - row - 1][n - col - 1] = matrix[col][n - row - 1]

            matrix[col][n - row - 1] = tmp