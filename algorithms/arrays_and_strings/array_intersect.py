def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    resultList = []
    for i in set1:
        if i in set2:
            resultList.append(i)
    for i in set2:
        if i in set1:
            resultList.append(i)
    return set(resultList)


data1 = [2,3,4,5,454,23,43425,463,643,53,534,6]
data2 = [3,4,3463,34,34,345,345,643,3,3]

print(intersection(data1, data2))