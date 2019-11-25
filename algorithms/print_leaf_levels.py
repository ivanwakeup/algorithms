'''
got asked this question in a LinkedIn interview. Basically we want to print each node of a tree, starting with the leaves.
if, after printing a leaf, a parent becomes a leaf, it would be printed in the NEXT level of the tree

example:
            A
          /  \
         B   C
        /   / \
       D   E  F
       \
       G

Would print, by line:
GEF => first leaves
DC =>
B => NEXT level of leaves
A => last leaf

we want to print the leaves from LEFT -> RIGHT in the tree


plan:
1 traversal to get max_depth of tree
then, build result array of arrays len(max_depth)
then traverse again postorder, appending leaf lines to their appropriate index in result array

'''


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class SolveLeafLevels:

    def __init__(self):
        pass

    def solve(self, root):
        if not root:
            return []
        depth = self.get_max_depth(root)
        result = [[] for _ in range(depth)]

        def do_solve(root, cur_level):
            if not root.left and not root.right:
                result[cur_level].append(root.val)
                return cur_level+1
            left_level, right_level = 0,0
            if root.left:
                left_level = do_solve(root.left, cur_level)
            if root.right:
                right_level = do_solve(root.right, cur_level)
            max_level = max(left_level, right_level)
            result[max_level].append(root.val)
            return max_level + 1

        do_solve(root, 0)
        self.print_solution(result)

    def get_max_depth(self, root):
        if not root:
            return 0
        return 1 + max(self.get_max_depth(root.left), self.get_max_depth(root.right))

    def print_solution(self, arr):
        for sub_arr in arr:
            print("".join(sub_arr))


t1 = TreeNode('A')
t1.left = TreeNode('B')
t1.right = TreeNode('C')
t1.left.left = TreeNode('D')
t1.left.left.right = TreeNode('G')
t1.right.left = TreeNode('E')
t1.right.right = TreeNode('F')

solver = SolveLeafLevels()

solver.solve(t1)