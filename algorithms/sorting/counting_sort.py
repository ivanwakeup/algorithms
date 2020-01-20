'''
counting sort is actually incredibly useful.

if we know our array contains only a small range of values, we can sort the array in near linear time.



INTUITIONS:

with counting sort, we create an auxillary array of length K (where k is the number of distinct values in the input)

we use this aux array to store the number of occurences of value i at the array slot aux[i]

once we have this array, we compute the prefix-sum of this array: HERES THE MAGIC, this prefix sum tells us the starting
position of the corresponding number in the output!

note: to get the starting position of any given num I, look at aux[i-1]. This is because the prefix-sum array tells us the starting
offset for the next number in the array.
'''

def counting_sort(arr):
    largest = max(arr)
    aux = [0 for _ in range(largest + 1)]

    for num in arr:
        aux[num]+=1

    for j in range(1, len(aux)):
        aux[j] = aux[j-1] + aux[j]

    result = [float('-inf') for _ in range(len(arr))]
    for num in arr:
        cnt = aux[num-1]
        result[cnt] = num
        aux[num-1] += 1

    return result



print(counting_sort([1, 4, 1, 2, 7, 5, 2, 9]))
