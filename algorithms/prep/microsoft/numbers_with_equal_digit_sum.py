'''
given an array of integers, return the maximum sum found of
any two pairs of digits that have their digits sum to the same value.

ex:
[51, 71, 17, 42] -> return 93, because 51 => 5+1 = 6 and 42 => 4+2 = 6, and 51 + 42 = 93
same applies 71 and 17, their digits sum to 8 respectively but their total sum is 88


plan:
iterate over numbers, and calculate each number's digit sum (constant time because numbers are guaranteed < 1bln
keep a hashmap of digit_sum => max_heap(digits)
iterate over hashmap keys, and pop the top two values off each heap, add them together, this is the answer
'''
from collections import defaultdict
from queue import PriorityQueue


def nums_equal_digit_sum(nums):
    d = defaultdict(PriorityQueue)
    for num in [str(x) for x in nums]:
        local_sum = 0
        for char in num:
            local_sum+=int(char)
        d[local_sum].put(-int(num))
    result = 0
    for key in d.keys():
        if d[key].qsize() < 2:
            continue
        local_result = 0
        popped = 0
        while not d[key].empty() and popped<2:
            local_result+= -d[key].get()
            popped+=1
        result = max(local_result, result)

    return result if result else -1

datas = [
[51, 71, 17, 42],
    [42,33,60],
    [51,32,43]
]
for data in datas:
    print(nums_equal_digit_sum(data))