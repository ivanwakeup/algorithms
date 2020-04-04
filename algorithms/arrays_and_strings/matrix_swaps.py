data = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


def transpose(matrix):
    for row in range(len(matrix)):
        for col in range(row, len(matrix[0])):
            tmp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = tmp


def swap_horizontals(matrix):
    row = 0
    while row < len(matrix):
        lo, hi = 0, len(matrix) - 1
        while lo < hi:
            matrix[row][lo], matrix[row][hi] = matrix[row][hi], matrix[row][lo]
            lo+=1
            hi-=1
        row+=1



transpose(data)
print(data)
swap_horizontals(data)
print(data)