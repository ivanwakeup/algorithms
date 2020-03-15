# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
just use a prev and a curr pointer

as we traverse, the CURR node should be reset to point to prev
we need to save TMP to keep track of where to go next
finally, move prev forward to CURR and set curr = tmp

at the end, PREV contains our answer because it will be the last node we processed (which would've pointed to NULL in original list,
meaning CURR contains NULL and not our new head at the end of iteration)
'''


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
