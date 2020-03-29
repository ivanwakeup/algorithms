'''
given two arrays A and B of the same length N,
find a "fair index" such that the fair index partitions BOTH arrays
such that the sums of A[:i], A[i+1:], B[:i], B[i+1:] are all equal


intuition:
this is the same problem as finding the equal sum partition index in array A, and then checking
if that partition index also splits B evenly

linear time approach:
compute the total sum of A and B
iterate over A, keeping track of the current sum in both A and B. if the sum(A)-cur_sum = cur_sum, we've found a partition
index in A so check that it's also valid in B. if so, return that index.
'''


def fair_indexes(a, b):
    if len(a) != len(b):
        raise ValueError
    suma = sum(a)
    sumb = sum(b)
    cursuma = 0
    cursumb = 0
    ans=0
    for i in range(len(a)-1):
        cursuma+=a[i]
        cursumb+=b[i]
        if cursuma == cursumb and suma-cursuma == cursuma and sumb-cursumb == cursumb:
            ans+=1
    return ans


datas = [
    ([4,-1,0,3], [-2,5,0,3], 2),
    ([2,-2,-3,3], [0,0,4,-4], 1),
    ([4,-1,0,3], [-2,6,0,4], 0),
    ([3,2,6], [4,1,6], 0),
    ([1,4,2,-2,5], [7,-2,-2,2,5], 2),
    ([0,0,0,0,0], [0,0,0,0,0], 4)
]

for data in datas:
    try:
        assert(fair_indexes(data[0], data[1]) == data[2])
        print(f"assertion succeeded for {data[0]}, {data[1]} == {data[2]}")
    except AssertionError:
        print(f"assertion failed for for {data[0]}, {data[1]} == {data[2]}")