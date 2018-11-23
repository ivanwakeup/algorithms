def gray_code(n):
    result = [0]
    for i in range(n):
        result = result + [2**i+x for x in result[::-1]]
    return result


print(gray_code(3))