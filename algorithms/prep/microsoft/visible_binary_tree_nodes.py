'''
In a binary tree, if in the path from root to the node A,
there is no node with greater value than A’s, this node A is visible.
We need to count the number of visible nodes in a binary tree.

Example 1:

Input:
        5
     /     \
   3        10
  /  \     /
20   21   1

Output: 4
Explanation: There are 4 visible nodes: 5, 20, 21, and 10.
Example 2:

Input:
  -10
	\
	-15
	   \
	   -1

Output: 2
Explanation: Visible nodes are -10 and -1.
'''

'''
approach
'''
from algorithms.utils import TreeNode, assert_test_cases

def count_visible_nodes(root):
    count = {'cnt':0}
    def do_find(root, maxval):
        if not root:
            return
        if root.val > maxval:
            count['cnt']+=1
        do_find(root.left, max(root.val, maxval))
        do_find(root.right, max(root.val, maxval))
    do_find(root, float('-inf'))
    return count['cnt']


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(21)
root.left.right = TreeNode(20)
root.right.left = TreeNode(1)

root2 = TreeNode(-10)
root2.right = TreeNode(-15)
root2.right.right = TreeNode(-1)

datas = [
    (root, 4),
    (root2, 2)
]

assert_test_cases(datas, count_visible_nodes)