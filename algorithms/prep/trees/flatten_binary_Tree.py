class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


data = TreeNode(1)
data.left = TreeNode(2)
data.right = TreeNode(3)


class Solution:
    def flatten(self, root: 'TreeNode') -> 'None':
        if not root.left and not root.right:
            return root
        tmp = self.flatten(root.right)
        l = self.flatten(root.left)
        l.right = tmp
        root.right = l
        root.left = None


sol = Solution()

sol.flatten(data)


