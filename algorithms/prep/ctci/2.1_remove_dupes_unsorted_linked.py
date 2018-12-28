'''
remove duplicates from an unsorted linked list.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


data = ListNode(3)
data.next = ListNode(4)
data.next.next = ListNode(3)
data.next.next.next = ListNode(4)
data.next.next.next.next = ListNode(2)

#result should be 1->3->2

#for 1->1 result should be 1

#for 3-4-3-4-2 result should be 3-4-2

'''
how will i know if the next element is a dupe?
i could create a hash set of which numbers are dupes by traversing the list once
i could also keep track of how many i need to delete

then i could traverse the list again and just remove the appropriate nodes the appropriate number of times


can we do it in a single pass?
yes, use a hash table and add element when you see it. if you see it again, delete it. if you see it again, add it back. etc

'''


def print_ll(head):
    cur = head
    str = ""
    while cur:
        str += "{}->".format(cur.val)
        cur = cur.next
    str += "NIL"
    print(str)


def remove_dupes_unsorted(head):
    if not head:
        return None

    seen = {head.val}
    cur = head.next
    prev = head
    while cur:
        if cur.val in seen:
            #we need to remove this node
            if cur.next:
                prev.next = cur.next
            else:
                prev.next = None
            cur = cur.next
        else:
            seen.add(cur.val)
            prev = cur
            cur = cur.next

    return head


remove_dupes_unsorted(data)
print_ll(data)