# Definition for singly-linked list.


'''
add lt to listnode definition

for each node in input, add it to heap
start popping off heap, when we pop add the popped node to a result
and add the popped node.next to the heap if it exists

to keep it simple, create a new listnode with the popped node's value
'''


class MyListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val < other.val


import heapq


class Solution:

    def mergeKLists(self, lists):
        new_lists = self.create_nodes(lists)
        heap = []
        for node in new_lists:
            heapq.heappush(heap, node)

        res = MyListNode('dummy')
        cur = res
        while heap:
            item = heapq.heappop(heap)
            cur.next = MyListNode(item.val)
            cur = cur.next
            if item.next:
                heapq.heappush(heap, item.next)
        return res.next

    def create_nodes(self, lists):
        res = []
        for item in lists:
            chain = MyListNode('dum')
            cur = chain
            while item:
                cur.next = MyListNode(item.val)
                cur = cur.next
            res.append(chain.next)
        return res

