'''
Alexa is given n piles of equal or unequal heights.
In one step, Alexa can remove any number of boxes from the pile which has the
maximum height and try to make it equal to the one which is just lower
than the maximum height of the stack.

Determine the minimum number of steps required to make all of the piles equal in height.

Example 1:

Input: piles = [5, 2, 1]
Output: 3
Explanation:
Step 1: reducing 5 -> 2 [2, 2, 1]
Step 2: reducing 2 -> 1 [2, 1, 1]
Step 3: reducing 2 -> 1 [1, 1, 1]
So final number of steps required is 3.

[1,2,3,4]:
[1,2,3,3]
[1,2,2,3]
[1,2,2,2]
[1,1,2,2]
[1,1,1,2]
[1,1,1,1]

[4, 4, 5, 2, 1]
solution:
put all items on a max heap.
pop items off the heap until the top of the heap is less than the current item
once it is, increment result by num_elements_off_heap, also keep track of how many elements we've popped off the heap
'''


import heapq
def min_steps_equal_boxes(boxes):
    heap = [-x for x in boxes]
    heapq.heapify(heap)
    result = 0
    popped = 0
    last = -heapq.heappop(heap)
    while heap:
        nxt = -heapq.heappop(heap)
        popped+=1
        if last > nxt:
            result+=popped
            last = nxt
    return result


datas = [
    ([4, 4, 5, 2, 1], 8),
    ([5,2,1], 3),
    ([1,1,1,1], 0),
    ([5,4,15,2,1], 10)
]

for data in datas:
    try:
        assert(min_steps_equal_boxes(data[0]) == data[1])
        print(f"assertion succeeded for {data[0]} == {data[1]}")
    except AssertionError:
        print(f"assertion failed for for {data[0]} == {data[1]}")


