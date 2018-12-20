from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

data = TreeNode(1)
data.left = TreeNode(2)
data.right = TreeNode(2)


def isSymmetric(root):
    if not root:
        return True
    queue = [root, root]
    while queue:
        node1 = queue.pop(0)
        node2 = queue.dequeue(0)
        if not node1 and not node2:
            continue
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        queue.append(node1.left)
        queue.append(node2.right)
        queue.append(node1.right)
        queue.append(node2.left)
    return True


print(isSymmetric(data))