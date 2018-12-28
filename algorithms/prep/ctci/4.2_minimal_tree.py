'''
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algo­
rithm to create a binary search tree with minimal height.
Hints: #79, #73, #7 76
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
approach:
we can do it recursively. set the root node to arr[mid]
build left half recursively with build_bst(arr[:mid]) and right half recursively

approach:
set root = arr[mid]
root.left = build_bst(arr[:mid])
root.right = build_bst(arr[mid:])

base case:
if len(arr) == 1:
return TreeNode(arr[0])

'''
def build_bst(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return TreeNode(arr[0])
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = build_bst(arr[:mid])
    root.right = build_bst(arr[mid+1:])
    return root


result = build_bst([2,70,91,100])

def print_tree(root):
    queue = [root]
    while queue:
        n_queue = []
        local = []
        while queue:
            node = queue.pop(0)
            local.append(node.val)
            if node.left:
                n_queue.append(node.left)
            if node.right:
                n_queue.append(node.right)
        queue = n_queue
        print(local)


print_tree(result)