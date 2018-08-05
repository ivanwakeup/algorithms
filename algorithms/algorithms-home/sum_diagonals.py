def diagonals(array):
    right_bound = len(array[0])
    bottom_bound = len(array)

    left_sum = 0
    right_sum = 0

    i = 0
    j = 0

    while i < right_bound and j < bottom_bound:
        left_sum += array[i][j]
        i += 1
        j += 1

    i = len(array[0]) - 1
    j = 0
    while i >= 0 and j < bottom_bound:
        right_sum += array[i][j]
        i -= 1
        j += 1

    return left_sum + right_sum


print(diagonals([[1,2,3], [1,2,3], [1,2,3]]))