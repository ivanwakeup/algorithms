class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

data = ListNode(1)
data.next = ListNode(1)
data.next.next = ListNode(2)
data.next.next.next = ListNode(2)
data.next.next.next.next = ListNode(2)
data.next.next.next.next.next = ListNode(3)

def deleteDuplicates(A):
    #both point to the node passed in
    head = current = A
    #not sure why previous is needed yet
    previous = None
    #loop until end of the list
    while current.next is not None:
        #check if current val is the same as the next val, need to set the head to the next val if so
        if current.val == current.next.val:
            if previous is None:
                head = current.next
            else:
                previous.next = current.next
        else:
            previous = current
        current = current.next
    return head


def printLL(ll):
    while ll:
        print ll.val
        ll = ll.next

print(printLL(deleteDuplicates(data)))