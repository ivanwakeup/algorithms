class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


data = TreeNode(1)
data.left = TreeNode(2)
data.right = TreeNode(3)


ref = data.left

data.left = None
print(ref.val)




