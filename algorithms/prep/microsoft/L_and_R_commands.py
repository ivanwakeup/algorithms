'''
with initial states for L and R, 0 and 1 respectively,

determine the minimum number of commands to make either L or R equal to a desired state
of a GIVEN value N.
"L" command changes L like L = 2*L-R
"R" command changes R like R = 2*R-L

example:
N = -11, ans => 4 by applying "L" -> "L" -> "R" -> "L"

    iterations:
    L=0, R=1
    L=-1, R=1
    L=-3, R=1
    L=-3, R=5
    L=-11, R=5


intuition:
we can model this like a graph with two starting states, and traverse it using BFS. From each start state 0
and 1, we can go to a new state by the L OR R command, so create a neighbor for each existing node based on the
L and R command formulas.

At any level of depth of the tree, if we find a node == N, we return our result
'''

from algorithms.utils import assert_test_cases


def l_and_r_cmd(n):
    queue = [[0,1,0]]
    while queue:
        node = queue.pop(0)
        if node[0] == n or node[1] == n:
            return node[2]
        L = 2*node[0]-node[1]
        R = 2*node[1]-node[0]
        queue.append([L,node[1],node[2]+1])
        queue.append([node[0],R,node[2]+1])


datas = [
    (-11, 4),
    (-22, 5)
]

assert_test_cases(datas, l_and_r_cmd)