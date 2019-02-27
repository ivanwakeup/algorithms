class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root.val
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root.val
        else:
            return left or right


data = TreeNode(3)
data.left = TreeNode(5)
data.right = TreeNode(1)
data.left.left = TreeNode(6)
data.left.right = TreeNode(2)
data.right.left = TreeNode(0)
data.right.right = TreeNode(8)
data.left.right.left = TreeNode(7)
data.left.right.right = TreeNode(4)


sol = Solution()

print(sol.lowestCommonAncestor(data, TreeNode(5), TreeNode(4)))





