'''
Given an array of roses. roses[i] means rose i will bloom on day roses[i].
Also given an int k, which is the minimum number of adjacent bloom roses required for a bouquet, and an int n, which is
the number of bouquets we need. Return the earliest day that we can get n bouquets of roses.

Example:
Input: roses = [3, 2, 1, 9, 3, 4, 1], k = 2, n = 2
Output: 4
Explanation:
day 1: [b, n, n, n, n, n, b]
The first and the last rose bloom.

day 2: [b, b, n, n, n, n, b]
The second rose blooms. Here the first two bloom roses make a bouquet.

day 3: [b, b, n, n, b, n, b]

day 4: [b, b, b, n, b, b, b]
Here the last three bloom roses make a bouquet, meeting the required n = 2 bouquets of bloom roses. So return day 4.



more examples:
[1,4,3,1,3,2,1], k=4, n=2
can't do it, because k*n > len(array)

assume it's always possible to make n boquets

[1,4,3,1,3,9,6], k=3, n=2
ans = 9, roses need to be adjacent to make a bouquet

[1,4,3,9,1,3,6], k=3, n=2
ans = 6

[9,7,1,2,1,1,6,1] k = 3, n = 2


what if we did n passes, finding the k group minimum each time? pretty shitty runtime.


'''

