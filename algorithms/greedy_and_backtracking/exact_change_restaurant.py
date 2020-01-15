'''
given a dictionary of menu items and their prices:
ex {'fruit': 2:15, 'fries': 2.75}
AND a target price, tp=15.05

find all combinations of the menu items that sum to that target price. WE CAN USE A MENU ITEM MORE THAN ONCE


can we do this with dynamic programming?

overlapping subproblems - ?

optimal substructure - an optimal solution to our problem involves an optimal solution to subproblems
    if we have TP left, and a static dictionary of items/prices, we know whether or not we can make any combinations

    in other words:
        let fd = food/price dictionary
        let tp = target price
        f(fd, tp) = the combinations we can achieve from our FD with TP remaining

        f(fd, tp) = cur_item + f(fd, tp-cur_item_price) for all cur_items

        base case:
            if tp == 0, append cur list of items to our result



this really seems like more of a greedy/backtracking algorithm than a dynamic programming one.



why isn't this dynamic programming?

1. because we're not maximizing/minimizing anything. we're just finding all combinations that add up to some amount
2. it's different from knapsack, because thats MAXIMIZING A value by picking items to bring along with you
3. this fits much better with a greedy "grab as many items as you can" approach, and see if we can make exact change


we could rephrase this question, perhaps, if we had an "enjoyment" factor associated with a food item
and we were trying to maximize our enjoyment given a dict of food/prices. but then this really just becomes
an example of knapsack again.

one other way to say it here is that we DONT EXHIBIT OPTIMAL SUBSTRUCTURE. Why?
because subproblems (the combinations we can achieve with a current "sack" and the dict of items)

'''

