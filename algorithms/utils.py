class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"{str(self.val)}->{str(self.next)}"


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_linked_list(elements):
    head = ListNode('dummy')
    curr = head
    for item in elements:
        curr.next = ListNode(item)
        curr = curr.next
    return head.next
