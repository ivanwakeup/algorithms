# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
for loop states:
1>2>3>4>5 goes to NULL<1   NULL<2
'''


class Solution:
    def reverseList(self, head):
        length = 0
        dum = head
        while head:
            length += 1
            head = head.next
        for _ in range(length):
            dum.next, dum, head = head, dum.next, dum
            '''
            this inline reversal is equivalent to:
            temp = dum.next
            dum.next = head
            head = dum
            dum = temp
            '''
        return head
