class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"{str(self.val)}->{str(self.next)}"


class Solution:

    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode('dummy')
        dummy.next = head
        curr = head.next
        prev = head
        while curr:
            #save the next node to consider
            nxt = curr.next
            runner = dummy
            if curr.val < prev.val:
                #runner moves forward until it precedes curr's new position
                while runner.next != curr and runner.next.val <= curr.val:
                    runner = runner.next
                #"swap" the unsorted node into the correct position
                if runner.next != curr:
                    prev.next = curr.next
                    tmp = runner.next
                    runner.next = curr
                    curr.next = tmp
            else:
                prev = curr
            '''prev represents the 'end' of the sorted portion of the linked list. 
               if we performed no swap on this iteration then that means prev and curr 
               were already in sorted order, so we move prev forward to the curr. If we performed a swap,
               prev needs to stay pointing to the node it points to, because that node now represents
               the end of the sorted portion of the list.'''
            curr = nxt
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