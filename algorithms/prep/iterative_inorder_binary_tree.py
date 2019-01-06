
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "TreeNode {}".format(self.val)


data = TreeNode(10)
data.left = TreeNode(5)
data.right = TreeNode(15)
data.right.left = TreeNode(6)
data.right.right = TreeNode(20)


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        stack = []
        start = root
        while start or stack:
            while start:
                stack.append(start)
                start = start.left
            bottom = stack.pop()
            result.append(bottom.val)
            if bottom.right:
                start = bottom.right
            print(result)

        return result


sol = Solution()

sol.isValidBST(data)