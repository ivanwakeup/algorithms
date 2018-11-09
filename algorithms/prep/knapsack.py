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
items = [4,8,5,2,9,3,1]


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


# print(knapsack(len(weights)-1, 10, {}))


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

def maximize_knapsack_value(c):
    weights = [5, 10, 3, 7, 4, 2, 1]
    values = [8, 12, 1, 9, 4, 1, 0]
    return do_maximize_knapsack(c, 0, weights, values)

def do_maximize_knapsack(cap, i, weights, values):

    if cap <= 0 or i < 0:
        return 0

    #this wont work, need to check first if i can include the ith item before i recurse
    included = 0
    if cap - weights[i] >= 0:
        included = values[i] + do_maximize_knapsack(cap-weights[i], i-1, weights, values)
    not_included = do_maximize_knapsack(cap, i-1, weights, values)
    result = max(included, not_included)

    return result

print(maximize_knapsack_value(10))









































