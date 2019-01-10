class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root, None]
        local_res = []
        while queue:
            node = queue.pop(0)
            # signifies the end of a level
            if not node:
                if not queue:
                    break
                queue.append(None)
                if not self.is_level_sym(local_res):
                    return False
                print(local_res)
                local_res = []
                continue

            if node == "Y":
                local_res.append(node)
                continue

            local_res.append(node.val)
            if node.left:
                queue.append(node.left)
            else:
                queue.append("Y")
            if node.right:
                queue.append(node.right)
            else:
                queue.append("Y")

        return True

    def is_level_sym(self, res):
        while len(res) > 1:
            if res.pop(0) != res.pop():
                return False
        return True


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

data = TreeNode(1)
data.left = TreeNode(2)
data.right = TreeNode(2)
data.left.left = TreeNode(3)
data.left.right = TreeNode(4)
data.right.left = TreeNode(4)
data.right.right = TreeNode(3)

sol = Solution()
sol.isSymmetric(data)