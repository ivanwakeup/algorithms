'''
Write a function that, given an array A of N integers, returns the lagest integer K > 0 such that both values K and -K exisit in array A. If there is no such integer, the function should return 0.

Example 1:

Input: [3, 2, -2, 5, -3]
Output: 3
Example 2:

Input: [1, 2, 3, -4]
Output: 0
'''

def largest(ints):
    hm = set()
    result = 0
    for int in ints:
        complement = ~int+1
        if complement in hm:
            result = max(result, abs(int))
        else:
            hm.add(int)
    return result

print(
    largest([1,2,3,-4])
)
