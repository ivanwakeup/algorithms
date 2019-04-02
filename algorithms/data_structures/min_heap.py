'''
what should i be able to do with a min heap?

heapify an array
'''

class MinHeap:

    def __init__(self, size, arr=None):
        self.size = size
        if arr:
            self.heap = self.heapify(arr)
        else:
            self.heap = []

    @staticmethod
    def heapify(arr):
        return arr

    '''
    returns the top element of the min heap. also re-heapifys the array
    '''
    def pop(self):
        pass


    '''
    what happens if our heap exceeds the maximum size allowable?
    '''


    '''
    promotes a key in the heap
    '''
    def promote(self, key):
        pass


    '''
    assume heap ABOVE index i is already a min heap,
    so we just need to insert this value into the heap.
    
    we need to find the smallest value from i, left(i), and right(i)
    
    set arr[i] to this value (swap it with the input i)
    and then recursively call min_heapify(self, largest) to make sure the
    value at i continues to "float down" if it doesn't obey the property.
    
    
    what is our base case?
    i == size_of_heap, in which case we terminate. why? because we're assuming everything above i is a valid min heap.
    therefore, there won't be any keys after i that are smaller than it
    '''
    def min_heapify(self, i):
        if i == self.size:
            return
        left = (2*i) + 1
        right = (2*i) + 2

        smallest = i

        if left <= self.size and self.heap[left] < self.heap[i]:
            smallest = left
            self.heap[left], self.heap[i] = self.heap[i], self.heap[left]

        if right <= self.size and self.heap[right] < self.heap[i]:
            smallest = right
            self.heap[right], self.heap[i] = self.heap[i], self.heap[right]

        #i wasn't the smallest, so we need to call __min_heapif
        if smallest != i:
            self.min_heapify(smallest)


    '''
    how do we know that a min-heap is valid?
    if the current key is less than both of its children, we are good
    '''
    def is_valid(self, min_heap):

        def validate(min_heap, i):
            if i >= len(min_heap):
                return True
            left = (2*i) + 1
            right = (2*i) + 2
            if left < len(min_heap) and min_heap[left] < min_heap[i]:
                return False
            if right < len(min_heap) and min_heap[right] < min_heap[i]:
                return False
            return min(validate(min_heap, left), validate(min_heap, right))

        return validate(min_heap, 0)





data = [1,3,2,7,4,8]
mh = MinHeap(len(data)-1, data)



#mh.min_heapify(2)


print(mh.is_valid(mh.heap))

