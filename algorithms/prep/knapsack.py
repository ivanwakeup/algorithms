'''
have a knapsack S
items with a size and value (s, v)
how to maximize the value of items in knapsack?

max_value = max(ssub0 + DP(ssub1toN,

def function knapsack(sack_size, cur_val, remaining)

recurrence for knapsack:
Max_value = VsubK
weights_array = W
values_array = V
VsubK(i, capacity) = max( VSubK(i-1, capacity-Wsubi), VSubK(i-1, capacity) ) FOR ALL i
'''

knapsack_size = 10

weights = [3,7,5,2,1,1,6]
items =   [4,8,5,2,9,3,1]


def knapsack(item_idx, capacity, memo):

    if item_idx + capacity in memo:
        return memo[item_idx + capacity]

    if item_idx < 0 or capacity == 0:
        result = 0
    else:
        didnt_add = knapsack(item_idx-1, capacity, memo)
        added = knapsack(item_idx-1, capacity - weights[item_idx], memo) + items[item_idx]
        result = max(didnt_add, added) if capacity - weights[item_idx] >= 0 else didnt_add

    memo[item_idx + capacity] = result
    return result


print(knapsack(len(weights)-1, 10, {}))


'''
have a knapsack S
items with a size and value (s, v)
how to maximize the value of items in knapsack?

step 1 - define subproblems

let DP(I, C) = the value attainable by including the current item I in the knapsack with C capacity remaining

DP(I, C) = max {
    include: value(I) + DP(I+1, C - W(I))
    not include: DP(I+1, C)
    for all items in knapsack
}
'''



'''bottom up knapsack implementation

1. represent values of the items on the rows, and weights of the items on the columns
2. iterating right on the columns, if the total weight of the ith item is > the value, you can't include it

ROWS: represent items[:i+1] that we're considering including
COLUMNS: represent the total capacity we have available in the knapsack

so, DP[i][j] says using items[:i+1], the max value we can achieve with J weight available is: ???

'''

def maximize_knapsack_bottom_up(capacity, values, weights):

    dp = [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]

    #what is the max value i can have with items[:0] and 0 capacity?
    dp[0][0] = 0

    for i in range(1, len(weights)+1):
        for j in range(1, capacity+1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], values[i-1]+dp[i-1][j-weights[i-1]])
    return dp[-1][-1]


print(maximize_knapsack_bottom_up(10, items, weights))











































