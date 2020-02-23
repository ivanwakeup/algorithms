'''
406. Queue Reconstruction by Height
Medium

Share
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater
than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

'''



'''
INTUITION:

1. sorting the people by decreasing height then by position allows us to maintain the "relative" order of heights
ex-- we know [7,1] must come after [7,0] in the output

2. keeping this processing order, if we just keep inserting the next person we examine at position K, python's insert()
function places the next item at THAT index and shifts everthing at K+1 to the right
'''

class Solution:
    def reconstructQueue0(self, people):
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output