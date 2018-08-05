def has_shift(a, b):
    for i in range(len(a)):
        if a[len(a)-i:] + a[:len(a)-i] == b:
            return True
    return False



print(has_shift("this", "isth"))