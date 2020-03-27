'''
In a binary tree, if in the path from root to the node A, there is no node with greater value than A’s,
this node A is visible. We need to count the number of visible nodes in a binary tree.

Input:
        5
     /     \
   3        10
  /  \     /
20   21   1

Output: 4
Explanation: There are 4 visible nodes: 5, 20, 21, and 10.


plan:
start at root and keep track of prev_best_sum, if curr node is greater than it we can increment result by one
'''

from algorithms.utils import TreeNode

def count_vis_nodes(root):
    count = {'cnt': 0}

    def do_count(root, prev):
        if not root:
            return
        if root.val > prev:
            count['cnt']+=1
        do_count(root.left, max(root.val, prev))
        do_count(root.right, max(root.val, prev))

    do_count(root, float('-inf'))
    return count['cnt']


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(20)
root.left.right = TreeNode(21)
root.right.left = TreeNode(1)

print(count_vis_nodes(root))


