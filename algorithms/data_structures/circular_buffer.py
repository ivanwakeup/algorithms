'''
a circular buffer is:

a fixed size arrays_and_strings that "evicts" keys when it is filled.

we can "append" keys to the current position in the buffer, if it is not full. if it is, we need to evict the "LRU" key

what are the buffer states:
empty - BEGIN and END are equal
below_capacity -
full - END is 1 less than BEGIN. that is. this also counts if END is at the last index and BEGIN is the start index
'''


class CircularBuffer:

    def __init__(self, size):
        if size < 1:
            raise ValueError("need positive size buffer!")
        self.buffer = [0 for _ in range(size+1)]
        self.begin = 0
        self.end = 0

    '''
    assume we overwrite values 
    '''
    def add(self, item):
        if (self.end + 1) % len(self.buffer) == self.begin:
            #we're full!
            print("buffer full, discarding {}".format(item))
            return
        self.buffer[self.end] = item
        #reassign self.tail, wrap it around if outside arrays_and_strings
        self.end = (1 + self.end) % len(self.buffer)

    def pop(self):
        result = self.buffer[self.begin]
        self.buffer[self.begin] = None
        self.begin = (1 + self.begin) % len(self.buffer)
        return result



cb = CircularBuffer(5)
for item in [1,2,3,4,5,6,7,8,9,10,11]:
    cb.add(item)
print(cb.pop())
print(cb.pop())
cb.add(2)
cb.add(3)
cb.add(4)
cb.pop()
cb.add(500)
print(cb.buffer)


'''
problems for "seqid cache" implementation:
1. we need to be able to quickly start reading at a given SeqId (use a hashmap for seqid -> array_pos)
    - lets assume pull(seqid, max_len): data just returns beginning at the seqid MAX_LEN number of elements, deleting along the way
    
2. 
'''