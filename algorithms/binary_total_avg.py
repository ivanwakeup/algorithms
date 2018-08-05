class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

data = TreeNode(3)
data.left = TreeNode(9)
data.right = TreeNode(20)
data.right.left = TreeNode(15)
data.right.right = TreeNode(7)


def average_of_levels(root):
    queue = [root]

    result = []

    while queue:
        sum = 0
        count = 0

        while queue:
            node = queue.pop(0)
            sum += node.val
            count += 1
            tmp = []
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        queue = tmp
        result.append(sum * 1.0 / count)
    return result


print(average_of_levels(data))