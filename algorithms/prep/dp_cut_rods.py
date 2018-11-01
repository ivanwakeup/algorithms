'''
problem:
we have a rod R of length N that we can cut into I pieces. Given a table of prices P, such that P(i) = price for i length of rod,
find the optimal revenue for the rod
'''

def find_max_revenue(n):
    table = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}
    memo = {1: 1, 2: 2}
    return helper(table, memo, n)

def helper(table, memo, n):
    if n < 3:
        return table[n]
    if n in memo:
        return memo[n]
    #RsubN = max revenue = max(PsubN, Psub1 + PsubN-1, Psub2 + PsubN-2, ....)
    revenue = table[n]
    for i in range(1, n):
        local = table[i] + helper(table, memo, n-i)
        revenue = max(revenue, local)
    memo[n] = revenue
    return revenue


print(find_max_revenue(8))