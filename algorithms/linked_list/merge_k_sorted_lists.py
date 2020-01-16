#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
divide and conquer approach
divide k sorted lists until there are 2 lists to merge
use a routine to merge those 2 lists

if l < h:
    left = merge(l, mid, lists)
    right = merge(mid+1, h, lists)

    return mergeTwoLists(left, right)

return list[low]
'''


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return []
        return self.merge(0, len(lists) - 1, lists)

    def merge(self, l, h, lists):
        if l == h:
            return lists[l]
        mid = (l + h) // 2
        left = self.merge(l, mid, lists)
        right = self.merge(mid + 1, h, lists)
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        dum = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dum.next