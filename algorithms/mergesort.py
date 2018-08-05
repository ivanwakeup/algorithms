def create_array(size=10, max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]


def merge(a, b):
    c = []

    a_idx, b_idx = 0,0

    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx = a_idx + 1
        else:
            c.append(b[b_idx])
            b_idx = b_idx + 1
    if a_idx == len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
    return c


def merge_sort(array):

    if len(array) <= 1:
        return array

    left, right = merge_sort(array[:len(array)/2]), merge_sort(array[len(array)/2:])

    return merge(left, right)

a = create_array()
print(merge_sort(a))