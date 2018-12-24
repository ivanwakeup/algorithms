def spiralOrder( matrix):
    if not matrix:
        return []

    right = len(matrix[0])
    down = len(matrix)
    left = 0
    up = 1
    result = []

    x, y = 0, 0

    while len(result) < len(matrix[0]) * len(matrix):
        while y < right:
            result.append(matrix[x][y])
            y += 1
        x += 1
        y -= 1
        right -= 1
        if left > right or up > down:
            break
        while x < down:
            result.append(matrix[x][y])
            x += 1
        y -= 1
        x -= 1
        down -= 1
        if left > right or up > down:
            break
        while y >= left:
            result.append(matrix[x][y])
            y -= 1
        x -= 1
        y += 1
        left += 1
        if left > right or up > down:
            break
        while x >= up:
            result.append(matrix[x][y])
            x -= 1
        x += 1
        y += 1
        up += 1
    return result



print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
