class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minDepth(root):
    if not root:
        return 0
    queue = [(root, 1)]

    while queue:
        node, level = queue.pop(0)
        if not node.left and not node.right:
            return level
        queue.append((node.left, level + 1))
        queue.append((node.right, level + 1))


def averageOfLevels(root):
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

        result.append(sum * 1.0 / count)
        queue = tmp
    return result


def mergeTrees(t1, t2):
    if not t1 and not t2:
        return
    if t1 and t2:
        t1.val = t1.val + t2.val
    elif t2:
        t1 = t2
    mergeTrees(t1.left, t2.left)
    mergeTrees(t1.right, t2.right)
    return t1


data = TreeNode(1)
data.left = TreeNode(3)
data.left.left = TreeNode(5)
data.right = TreeNode(2)

data2 = TreeNode(2)
data2.left = TreeNode(1)
data2.right = TreeNode(3)
data2.left.right = TreeNode(4)
data2.right.right = TreeNode(7)


print(mergeTrees(data,data2))
