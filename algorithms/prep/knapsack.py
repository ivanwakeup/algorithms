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


print(knapsack(len(weights)-1, 10, {}))