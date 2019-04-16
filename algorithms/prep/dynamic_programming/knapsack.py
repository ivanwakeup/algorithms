'''
given two equal-length arrays, ITEMS and VALUES, where each index i represents an (ITEM, VALUE) pair

AS WELL AS

a total_capacity in your knapsack available, tc = 15

what is the maximum VALUE you can achieve by taking items in your knapsack?


how does this exhibit:

optimal substructure - optimal solutions to subproblems can give us the OPTIMAL solution to our main problem

let MV(tc, items) be the max value achieveable with a total capacity (tc) and items

MV(tc, items, values) = max {
    values[i] + MV(tc - items[i], items, values)
} for all i in items/values



HOW IT EXHIBITS OPTIMAL SUBSTRUCTURE

how can the optimal solution to a subproblem, say

MV(tc, items - items[i], values, cur_total_val + value[item[i]])

help us solve MV(tc, items, values, cur_total_val)?


because for any given item/value dict, if we have some capacity available C and we know the answer that maximizes
MV, how does that value change when we add an item/total capacity?

well, we can either INCLUDE that item in what we take (if we have the capacity for it)
or we cannot include that item and the MV result for our main problem is the same as it was for the subproblem.

'''


weights = [7,3,9,9,11,50,2,34,6,77,86,1,3,7,4,46,2,4,4,4,4,4]
values = [7,3,9,9,11,50,2,11,6,77,86,55,3,22,3,55,2,4,1,23,66,7]


'''
approach:

consider each item
two cases:
    - include item if capacity allows, so MV = value[item] + MV(items-item, values, capacity-item)
    - don't include, so MV is just MV(without_cur_item)
    
how do we encode which value we're considering?
keep track of J, the element in the array to include or not 



how can we memoize? this is the DP part.

we use the index i and the capacity left remaining to memoize the solution. why?
because we are considering elements from i onwards in the array.

the fact that we don't know if the current element should be in the result or not is what gives us OVERLAPPING SUBPROBLEMS.

at each item, we need to find the max of both including and not including it. if you draw out the recursion tree you'll see that
you recalculate the same answer each time

of course the recursive approach takes call stack space
'''

'''
NON-MEMOIZED BRUTE FORCE
'''
def maximize_value(weights, values, capacity):

    call_dict = {'val': 0}
    def do_max(weights, values, cap, i):

        if i >= len(weights):
            return 0
        cur_item_value = values[i]

        not_includes_cur = do_max(weights, values, cap, i+1)
        includes = cur_item_value + do_max(weights, values, cap-weights[i], i+1) if cap-weights[i] >= 0 else not_includes_cur

        call_dict['val']+=1
        return max(not_includes_cur, includes)


    result = do_max(weights, values, capacity, 0)
    print(call_dict['val'])
    return result


print("call_count and result for non-memo solution\n", maximize_value(weights, values, 10), "\n\n\n")



'''
MEMOIZED VERSION
'''
def maximize_value(weights, values, capacity):

    call_dict = {'val': 0}
    memo = {}
    def do_max(weights, values, cap, i):
        key = (i, cap)
        if key in memo:
            return memo[key]
        if i >= len(weights):
            return 0
        cur_item_value = values[i]

        not_includes_cur = do_max(weights, values, cap, i+1)
        includes = cur_item_value + do_max(weights, values, cap-weights[i], i+1) if cap-weights[i] >= 0 else not_includes_cur

        call_dict['val']+=1
        result = max(not_includes_cur, includes)
        memo[key] = result
        return result


    result = do_max(weights, values, capacity, 0)
    print(call_dict['val'])
    return result


print("call_count and result for memoized solution\n", maximize_value(weights, values, 10), "\n\n\n")



'''
what about a bottom-up approach?

we have our recurrence relation:

MV(weights, items, i, cap) = max {
    MV(weights, items, i+1, cap) -> didn't include item
    value[i] + MV(weights, items, i+1, cap-weights[i]) -> did include item
} for all i


start from the beginning of the array and ask the same questions:
1. what is the MV by including item[i]?
2. what is the MV by not including it?

if we build up an [][] and let the columns be the CAPACITY and the rows be the INDEX of the item we're considering, we can answer
the above question.

update each cell (i, j) in the matrix by:

for the first row, we know we're only considering the first item so the MV is just the value of that item, beginning
when we have enough capacity

for each subsequent row, the value (once we have enough capacity to include the item) is either:
    value[i-1][j] <- we didn't include the item
    value[i-1][j-weight[i]] <- we included it, and now we check the previous BEST we were able to do with the capacity
    we have remaining after subtracting the current item.

'''

def bottom_up_knapsack(weights, values, capacity):
    if capacity <= 0:
        return 0
    i = len(weights) - 1
    dp = [[0 for _ in range(capacity+1)] for _ in range(i+1)]

    #fill out top row
    for x in range(len(dp[0])):
        dp[0][x] = values[0] if weights[0] <= x else 0



bottom_up_knapsack(weights, values, 15)