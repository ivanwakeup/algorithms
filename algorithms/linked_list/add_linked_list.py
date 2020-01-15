class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

data = ListNode(9)
data.next = ListNode(3)
data.next.next = ListNode(2)

data2 = ListNode(9)
data2.next = ListNode(3)
data2.next.next = ListNode(2)


def addFromLinked(l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry%10)
        cur = cur.next
        carry //= 10
    return dummy.next


print(addFromLinked(data, data2))





