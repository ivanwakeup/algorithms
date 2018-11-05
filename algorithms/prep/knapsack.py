knapsack = {
    5: 10,
    2: 3,
    4: 6,
    10: 21,
    1: 2
}

backpack_limit = 10
#what is the optimal combination of items in the knapsack?
'''
recurrence for knapsack:
let solution V(K, W) = max value for knapsack and weight limit
let I = index of current item
let RV(K, W, I) = recursive max value of knapsack starting with item I
V(K, W) = max(RV(, V(K, W))
'''

#brute force algorithm
def find_max_value_1(max_limit, cur, item, value):
    #greedily evaluate all possibilities of items up until limit is reached
    if cur + item[0] > max_limit:
        return value
    cur = cur + item[0]
    for key, val in knapsack.items():
        new_value = find_max_value_1(max_limit, cur, (key, val), value + val)
        value = max(new_value, value)
    return value

def find_max_bf():
    return find_max_value_1(backpack_limit, 0, (0, 0), 0)

print(find_max_bf())

#end brute force