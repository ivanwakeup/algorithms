'''
given an array where every int appears 3 times except for 1, return that 1 number
in linear time and constant space

[6,1,3,3,3,6,6,9,9,9]
result = 1

constant space = no hash map

could maybe do multiple passes on the array
we don't know if its the smallest/largest element that will appear

could use a bit vector maybe?
but all elements appear an odd number of times, so we wont be able to jsut "See whats left" at the e

bit tricks:
get, set and unset bit


approach:
[6, 2, 2, 2]

'''

def find_non_dup(arr):
    #we can only have a single non dup element if the size of the array is 3n + 1
    if (len(arr)-1)%3 != 0:
        return -1
    ones = 0
    twos = 0
    for i in range(len(arr)):
        common = ones & arr[i]
        twos |= common
        ones ^= arr[i]
        not_threes = ~(ones & twos)
        ones &= not_threes
        twos &= not_threes
    return ones

print(find_non_dup([10,20,10,30,10,30,30]))
