def all_subarrays(arr):

    if not arr:
        return []

    result = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            result.append(arr[i:j+1])
    return result


print(all_subarrays([1,2,3]))


def all_subset_partitions(arr):

    if not arr:
        return []

    result = []
    for i in range(1,len(arr)-1):
        for j in range(i, len(arr)):
            left = data[:i] + [data[j]]
            right = data[i:j] + data[j+1:]
            result.append((left, right))
    return result


data = [1,6,11,5]
print(all_subset_partitions(data))


def gcd(a, b):
    if a == 0 or b == 0:
        return a or b
    if a > b:
        return gcd((a%b), b)
    else:
        return gcd((b%a), a)

print(gcd(10, 6))


