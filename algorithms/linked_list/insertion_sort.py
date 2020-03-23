class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"{str(self.val)}->{str(self.next)}"


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''

'''
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        p = head.next
        pre = head
        while p:
            nxt = p.next
            q = dummy
            if p.val < pre.val:
                #move q forward until it preceeds insertion point
                while q.next.val < p.val:
                    q = q.next
                #delete p from its position
                pre.next = p.next
                tmp = q.next
                #insert p after q
                q.next = p
                p.next = tmp
            #only update pre if we didn't insert. if we did insert, pre points to the
            #end of the sorted list.
            else:
                pre = p
            p = nxt
        return dummy.next


def build_linked_list(elements):
    head = ListNode('dummy')
    curr = head
    for item in elements:
        curr.next = ListNode(item)
        curr = curr.next
    return head.next


items = [1,2,4,3,1,5]
ll_head = build_linked_list(items)
sol = Solution()

print(
    sol.insertionSortList(ll_head)
)