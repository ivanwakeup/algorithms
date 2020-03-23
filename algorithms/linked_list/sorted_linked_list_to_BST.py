from algorithms.utils import ListNode, build_linked_list, TreeNode


class Solution:
    def sortedListToBST(self, head):
        return self.do_form(head)

    def do_form(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        root = TreeNode(slow.val)
        root.left = self.do_form(head)
        root.right = self.do_form(slow.next)
        return root

data = [-10,-3,0,5,9]

ll_head = build_linked_list(data)
sol = Solution()
print(
    sol.sortedListToBST(ll_head)
)
