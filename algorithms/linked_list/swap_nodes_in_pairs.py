# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
swap 1 and 2
dum.next should point at 2
2 should point at 1
head should point to 3
1 should point to 3
dum = cur = ListNode(0)
dum.next = head
while head and head.next:
    tmp = head.next
    cur.next = tmp
    cur = tmp.next
    tmp.next = head
    head = cur

return dum.next
'''


class Solution:
    def swapPairs(self, head):
        dum = prev = ListNode(0)
        dum.next = head
        while head and head.next:
            tmp = head.next
            # set head.next to 3rd node. now 1 -> 3
            head.next = tmp.next
            prev.next = tmp
            tmp.next = head
            head = head.next
            # still 2->3, so set cur to 3
            prev = tmp.next
        return dum.next