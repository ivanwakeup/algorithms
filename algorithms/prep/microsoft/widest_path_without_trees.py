'''
the problem description is fucking long, so look here:
https://leetcode.com/discuss/interview-question/447448/

but basically, we are given:
two arrays X and Y of equal length
any index i in either array corresponds to a coordinate of a "tree" in a forest:
(x[i], y[i])

we want to find the "widest" possible vertical gap we can make between two trees
such that there is no tree between those two trees:

ex:
X=[5,5,5,7,7,7] Y=[3,4,5,1,3,7]
ans = 2, if we look just at the X array we see that the widest gap without any trees in the middle is
between [5,7]

ex:
X=[6,10,1,4,3] Y=[2,5,3,1,6]
ans=4, between the interval [6,10] there are no other trees and it forms our widest gap
again, the Y coordinates don't matter.


intuitions:
1. Y coordinate array doesn't affect if trees "overlap", so it doesn't matter for this problem
2. we could sort the X array, and just calculate the range between i and i-1 and take the largest.

'''

def widest_path_between_trees(X, Y):
    X.sort()
    ans = 0
    for i in range(1, len(X)):
        ans = max(ans, abs(X[i]-X[i-1]))
    return ans


datas = [
    ([6,10,1,4,3], [2,5,3,1,6])
]

for data in datas:
    print(
        widest_path_between_trees(data[0], data[1])
    )

