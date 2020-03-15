'''

0-1 version of knapsack, can't take
given a list of [item_weights, values] and a max_weight, maximize the total value we can achieve by adding items
to the knapsack

ex:
item_weights = [7,3,9,1,2]
item_values =  [6,4,2,1,4]

backpack_capacity = 15


recursive relation:

knapsack(weights, values, i, cap_remaining) = values[i] + knapsack(weights, values, i+1, cap_remaining-weights[i])
'''


def knapsack(weights, values, capacity):

    def maximize(weights, values, i, cap):
        if i >= len(weights):
            return 0
        take_it = values[i] + maximize(weights, values, i+1, cap-weights[i])
        dont_take = maximize(weights, values, i+1, cap)
        return max(take_it, dont_take)

    return maximize(weights, values, 0, capacity)


weights = [7,3,9,1,2]
values = [6,4,2,1,4]
cap = 15


print(knapsack(weights, values, cap))