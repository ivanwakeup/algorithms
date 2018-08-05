class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def avg(root):
    queue = [root]
    result = []
    while queue:
        sum = 0
        count = 0
        temp = []
        while queue:
            node = queue.pop(0)
            sum += node.val
            count += 1
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        queue = temp
        result.append(sum * 1.0 / count)
    return result


data = TreeNode(1)
data.left = TreeNode(2)
data.right = TreeNode(3)


print(avg(data))
