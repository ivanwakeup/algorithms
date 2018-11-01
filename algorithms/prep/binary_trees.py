class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "TreeNode Value: {}<-{}->{}".format(self.left, self.val, self.right)


class BinarySearchTree:

    def __init__(self, node=None):
        self.root = None
        if node:
            self.root = node

    def search(self, val):
        root = self.root
        while root:
            if root.val == val:
                print("Found value! {} at {}".format(root.val, id(root)))
                return root.val
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        print("Couldn't find value: {}".format(val))
        return -1

    def insert(self, val):
        def insert_helper(val, root, parent):
            #assume unique values
            if not root:
                root = TreeNode(val)
                if parent and parent.val < root.val:
                    parent.right = root
                elif parent:
                    parent.left = root
                return

            if root.val == val:
                print("This value already exists in the tree!: {}".format(val))
                return
            elif root.val > val:
                return insert_helper(val, root.left, root)
            return insert_helper(val, root.right, root)

        insert_helper(val, self.root, None)

    def delete(self, val):
        pass

    def transplant(self, node1, node2):
        pass

    def successor(self, node):
        pass

    def to_inorder_array(self):
        pass

    def to_preorder_array(self):
        pass

    def to_postorder_array(self):
        pass


data = TreeNode(3)
data.left = TreeNode(2)
data.right = TreeNode(4)
data.left.left = TreeNode(1)
data.right.right = TreeNode(5)

tree = BinarySearchTree(data)

tree.search(5)
tree.search(10)


tree.insert(7)

tree.search(7)
tree.search(5)
tree.search(1)

