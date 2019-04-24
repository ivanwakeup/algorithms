'''
given two equal-length arrays, ITEMS and VALUES, where each index i represents an (ITEM, VALUE) pair

AS WELL AS

a total_capacity in your knapsack available, tc = 15

what is the maximum VALUE you can achieve by taking items in your knapsack?


how does this exhibit:

optimal substructure - an optimal solution to our problem involves an optimal solution to our subproblems

let MV(tc, items) be the max value achieveable with a total capacity (tc) and items

MV(tc, items, values) = max {
    values[i] + MV(tc - items[i], items, values)
} for all i in items/values

is this true?

'''

