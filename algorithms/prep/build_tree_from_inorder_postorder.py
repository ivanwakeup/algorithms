
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.idx = len(postorder) - 1
        # we have elements left to build
        return self.do_build(inorder, postorder)

    def do_build(self, inorder, postorder):
        if self.idx < 0 or not inorder:
            return
        root = TreeNode(postorder[self.idx])
        self.idx -= 1
        inorder_slice = inorder.index(root.val)
        root.right = self.buildTree(inorder[inorder_slice + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_slice], postorder)
        return root


sol = Solution()
sol.buildTree([9,3,15,20,7], [9,15,7,20,3])