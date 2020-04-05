# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
we use a left->right->curr traversal, because we need two answers from each subtree:
1. what is the max we can achieve by robbing the subtree root
2. what is the max we can achieve by not robbing the subtree root

for each subtree.

one important detail is:
we return max(not_rob_here, rob_here) for the value of the current subtrees result[0], because
the BEST we can do at the current subtree we're considering IF we rob the root still might not include the root.

in other words, rob_here really tracks "what is the BEST we can do here if we include the current root in the decision?"=> it means MAYBE selecting the current root but MAYBE not.

and the value not_rob_here doesn't consider the current root at all.

'''


class Solution:
    def rob(self, root: TreeNode) -> int:
        def do_rob(root):
            if not root:
                return (0, 0)

            rob_left, not_rob_left = do_rob(root.left)
            rob_right, not_rob_right = do_rob(root.right)

            rob_here = root.val + not_rob_left + not_rob_right
            not_rob_here = rob_left + rob_right

            return (max(not_rob_here, rob_here), not_rob_here)

        return max(do_rob(root))