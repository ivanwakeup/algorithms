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

    def delete(self, key):
        root = self.root
        if not root:
            return None
        start = prev = root
        while start:

            if start.val == key:
                if not start.right:
                    if prev.left == key:
                        prev.left = start.left
                    else:
                        prev.right = start.right
                    break
                else:
                    next = self.find_min(start.right)
                    next.left = start.left
                    next.right = start.right
                    if prev.left == key:
                        prev.left = next
                    else:
                        prev.right = next
                    break

            elif start.val < key:
                prev = start
                start = start.right
            else:
                prev = start
                start = start.left

        return root

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def transplant(self, node1, node2):
        #should replace the tree rooted at node1 with node2 and node2 with node1
        pass

    def successor(self, node):
        #find node with the smallest key greater than given node
        if not node.right:
            return None
        start = node.right
        while start:
            prev = start
            start = start.left
        return prev

    def to_array(self):
        root = self.root
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            result.append(node.val)
        return result

    def to_inorder_array(self):
        pass

    def to_preorder_array(self):
        pass

    def to_postorder_array(self):
        pass




data = TreeNode(5)
data.left = TreeNode(3)
data.right = TreeNode(6)
data.left.left = TreeNode(2)
data.left.right = TreeNode(4)
data.right.right = TreeNode(7)

tree = BinarySearchTree(data)

tree.search(5)
tree.search(10)


#tree.insert(7)

tree.search(7)
tree.search(5)
tree.search(1)

#tree.delete(3)

arr = tree.to_array()

print(arr)


