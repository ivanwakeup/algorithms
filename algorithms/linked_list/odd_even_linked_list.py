class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"{str(self.val)}->{str(self.next)}"

'''
intuition:
use a 
'''


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        prev = None
        even = head.next
        even_ptr = even
        while odd:
            prev = odd
            next_node = None
            if even:
                odd.next = even.next
                next_node = odd.next
            if even and even.next:
                even.next = even.next.next
                even = even.next
            odd = next_node

        prev.next = even_ptr
        return head


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
one.next = two
two.next = three
three.next = four
four.next = five

sol = Solution()

print(
    sol.oddEvenList(one)
)