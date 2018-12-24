'''

Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps.

Examples :

Input:  n = 3
Output: 4
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step

Input:  n = 4
Output: 7
'''

'''
examples:
[1] = 1 way (only with 1 step)
[2] = 2 ways (1+1 step, 2 step)
[3] = 4 ways (1+1+1, 1+2, 2+1, 3)
[4] = 7 ways (1+1+1+1, 1+2+1, 1+1+2, 2+2, 3+1, 1+3, 2+1+1)

brute force?:

not sure how to "brute force" this initially
brute force is essentially with recursion
need to actually generate all the ways to take steps

for 4 ways,

its not just 1 + num_ways(3)

num_ways(n, i) = num_ways(n-i, i+1)

//only one way to take 1 step
if n == 0:
    return 1
    
else:
for x in range(i, n):
    ways += recur(n-x, x+1)

ways = 0
for x in range(1, 4):
    if n - x > 0:
        ways += recur(n-x)
return ways

what is the runtime?

should be something like 3^n before memoization,
n^3 with memoization
'''

def num_ways(n, memo):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]

    ways = 0
    for x in range(1, 4):
        if n - x >= 0:
            ways += num_ways(n-x, memo)
    memo[n] = ways
    return ways

#print(num_ways(10, {}))


'''
can solve iteratively?

#store the num ways for prev results in an array
dp[i] = num ways to take i steps

dp[0] = 1
dp[1] = 1

need to check for each possible step value?

for i in range(2, n+1):
    ways = 0
    for j in range(1, 4):
        if i - j >= 0:
            ways += dp[i-j]
    dp[i] = ways
return dp[-1] 
'''

def num_ways_iter(n):

    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        ways = 0
        for j in range(1, 4):
            if i - j >= 0:
                ways += dp[i - j]
        dp[i] = ways

    return dp[-1]

print(num_ways_iter(10))