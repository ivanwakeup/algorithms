'''

coin change recurrence:
problem statement - how many ways can you make change for a value N with some set of coins S = {s1, s2, s3.....sM}

num_ways(n, S) = num_ways(n - s1, S)

base case:
n == 0 and s == 0:
    return 1

'''

def coin_changer(n, coins):

    if n == 0 and not coins:
