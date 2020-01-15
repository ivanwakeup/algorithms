#implemented using a heap
'''
A heap is a tree like data structure where each child node left(i) and right(i) are less than or greater than the current node (max or min heap)
heaps support the following operations:
max-heapify - start from root, let value "float down" by recursively calling max-heap
get-left-node
get-right-node
insert?
you can make a heap from an arrays_and_strings by calling max-heapify for each element [0....n//2]


heap operations needed for priority queue:
extract-max-value - store max value, swap for node at the bottom of heap, and call max-heapify
insert(key)
peek-max-value
'''

class MaxPriorityQueue:

    def __init__(self):
        self.heap = [0]
        self.heap_size = 0

    def left(self, i):
        return (i*2) + 1

    def right(self, i):
        return i*2 + 2

    def parent(self, i):
        return (i-1) // 2

    #ensures the heap is always a valid max heap by comparing 3 values: the current val, and the left and right child. by swapping the cur val with the largest of the 3
    #vals, we guarantee as we recurse that we have a valid max heap
    def heapify(self, i):
        arr = self.heap
        left = self.left(i)
        right = self.right(i)
        largest = i
        if left <= self.heap_size-1 and arr[left] > arr[largest]:
            largest = left
        if right <= self.heap_size-1 and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(largest)

    #push an element by inc heap_size, set that position to neg infinity, and then "promote" they key of the new element added
    def push(self, ele):
        self.heap_size += 1
        self.heap.append(float('-inf'))
        self.promote(self.heap_size-1, ele)

    #easy, just grab the first element, set the first element now to the last element, then "heapify" it. finally return the first element
    def pop(self):
        if not self.heap_size:
            raise ValueError
        max = self.heap[0]
        self.heap[0] = self.heap[self.heap_size-1]
        self.heap_size -= 1
        self.heapify(0)
        return max

    #the pos signifies the rank within the queue of the element. with this arrays_and_strings-based implementation,
    #we first check to make sure the pos we increase isn't already higher
    #then, we set the pos to new key and "float up" via the parent until the parent is greater than the key we inserting (its now a valid max heap at that point)
    def promote(self, pos, key):
        if key < self.heap[pos]:
            raise ValueError
        self.heap[pos] = key
        while pos > 0 and self.heap[self.parent(pos)] < self.heap[pos]:
            self.heap[self.parent(pos)], self.heap[pos] = self.heap[pos], self.heap[self.parent(pos)]
            pos = self.parent(pos)


data = [3,2,1,5,4,45,22,456,72]

pq = MaxPriorityQueue()

pq.heap = data + [float('-inf')]
pq.heap_size = len(data)

for i in range(len(data)//2, -1, -1):
    pq.heapify(i)

print(pq.heap)

