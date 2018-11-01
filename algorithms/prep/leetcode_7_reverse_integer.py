def reverse(x):
    max_size = 2 ** 31 - 1
    neg_max_size = -(2 ** 31) - 1
    if x < neg_max_size or x > max_size:
        return 0
    out = 0
    while x > 0:
        if x % 10 > 0:
            tmp = x % 10
            x = x / 10
            out = out * 10 + tmp
    return out


print(reverse(123))