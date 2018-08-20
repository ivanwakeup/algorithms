
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

data = TreeNode(4)
data.left = TreeNode(1)
data.right = TreeNode(2)

data2 = TreeNode(4)
data2.left = TreeNode(1)
data2.right = TreeNode(2)


def isSubtree( s, t):
    return helper(s, t)

def helper( s, t):
    if s.val == t.val:
        if check(s, t):
            return True
    if s.left:
        if helper(s.left, t):
            return True
    if s.right:
        helper(s.right, t)
    return False

def check( t1, t2):
    if not t1 and not t2:
        return True
    if t1.val == t2.val:
        return check(t1.left, t2.left) and check(t1.right, t2.right)
    else:
        return False

print(isSubtree(data, data2))