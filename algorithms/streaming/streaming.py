import socket
import json
import sys 


def stream_bytes_from_address(host: str, port: str):

    sock = socket.create_connection(("localhost", 9000))
    buffer = bytes()
    return


def generate_random_number_stream(low, high):
    import random
    num_events = 0
    while num_events <= high:
        yield random.randint(low, high)
        num_events+=1

import random
class RandomNumberStream:

    def __init__(self, low, high) -> None:
        self.num_events = 0
        self.low = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.num_events < self.high:
            self.num_events+=1
            return random.randint(self.low, self.high)
        else:
            raise StopIteration


st = RandomNumberStream(1, 100)

import heapq

def compute_stream_statistics(number_stream):
    running_sum = 0
    running_avg = 0
    items_consumed = 0

    max_h = []
    min_h = []
        
    for item in number_stream:
        running_sum+=item
        items_consumed+=1
        running_avg = float(running_sum / items_consumed)

        if not max_h or item<=max_h[0]:
            heapq.heappush_max(max_h, item)
        else:
            heapq.heappush(min_h, item)

        if len(max_h) > len(min_h) + 1:
            heapq.heappush(min_h, heapq.heappop_max(max_h))
        elif len(min_h) > len(max_h) + 1:
            heapq.heappush_max(max_h, heapq.heappop(min_h))

        if len(max_h) == len(min_h):
            median = (max_h[0] + min_h[0]) / 2
        elif len(max_h) > len(min_h):
            median = max_h[0]
        else:
            median = min_h[0]

            

        print(f"running_sum is {running_sum}")
        print(f"running_avg is {running_avg}")
        print(f"running median is {median}")

#compute_stream_statistics(st)



def resevoir_sample(stream, k):
    '''
    function to sample K elements from a stream, with each element in the stream having equal
    probability of appearing in the resulting sample
    '''
    import random
    buffer = []
    result = []
    proc=0
    for item in stream:
        proc+=1
        if len(result) < k:
            result.append(item)
        else:
            should_appear = True if random.random() < (k/proc) else False
            if should_appear:
                result[random.randint(0, k-1)] = item
        yield result
                


# for item in resevoir_sample(RandomNumberStream(1, 100), 5):
#     print(item)


from queue import PriorityQueue
from dataclasses import dataclass
from collections import Counter

@dataclass
class StreamItem:
    key: str
    count: int

def top_k_elements(stream, k):
    hm = {}
    pq = PriorityQueue()
    for item in stream:
        if item in hm:
            hm[item].count+=1
        else:
            hm[item] = StreamItem(item, 1)

        si = hm[item]
        pq.put((-si.count, si.key))
        result = []
        i = 0
        while i < min(k, len(hm)) and not pq.empty():
            item = pq.get()
            if abs(item[0]) != hm[item[1]].count:
                continue
            else:
                result.append(hm[item[1]].key)
                i+=1

        for item in result:
            put_back = (-hm[item].count, hm[item].key)
            pq.put(put_back)
        print(hm)
        yield result

from pqdict import pqdict

def top_k_elements_indexed_pq(stream, k):
    pq = pqdict()
    for item in stream:
        if item in pq:
            pq[item]-=1
        else:
            pq[item]=-1

        result = []
        for _ in range(k):
            if pq:
                item = pq.popitem()
                result.append(item)

        for item in result:
            pq[item[0]] = item[1]

        yield [x[0] for x in result]


from collections import defaultdict
def top_k_from_stream_count_buckets(stream, k):
    hm = defaultdict(set)
    seen = {}
    max_seen = 1
    for item in stream:
        if item not in seen:
            seen[item] = 1
            hm[1].add(item)
        else:
            count = seen[item]
            hm[count].remove(item)
            if not hm[count]:
                del hm[count]
            hm[count+1].add(item)
            seen[item]+=1
            max_seen = max(max_seen, seen[item])

        if len(seen) <= k:
            yield list(seen)
        else:
            result = []
            highest = max_seen
            added_count = 0
            while added_count < k:
                nxt = hm[highest]
                for key in nxt:
                    result.append(key)
                    added_count+=1
                    if added_count==k:
                        break
                highest-=1
            yield result



class StreamItemNode:

    def __init__(self, key, count, sentinel=False):
        self.key = key
        self.count = count
        self.next = None
        self.prev = None
        self.sentinel = sentinel

class DLLContainer:

    def __init__(self):
        self.head = StreamItemNode(None, None, True)
        self.tail = StreamItemNode(None, None, True)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0

    def insert_node(self, node, front=False):
        if front:
            next = self.head.next
            self.head.next = node
            node.next = next
            next.prev = node
            node.prev = self.head
        else:
            prev = self.tail.prev
            prev.next = node
            node.next = self.tail
            self.tail.prev = node
            node.prev = prev
        self.len+=1

    def remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.len-=1

    def insert_after(self, node, after):
        next = after.next
        node.prev = after
        node.next = next
        next.prev = node
        after.next = node
        self.len+=1

    def insert_before(self, node, before):
        prev = before.prev
        prev.next = node
        node.next = before
        before.prev = node
        node.prev = prev
        self.len+=1


class BucketNode:

    def __init__(self, count, sentinel=False):
        self.count = count
        #this needs to be a StreamItemNodeContainer
        self.item_list: DLLContainer = DLLContainer()
        self.next = None
        self.prev = None
        self.sentinel = sentinel



def top_k_from_stream_dlls(stream, k):
    seen = {}
    buckets = {}
    
    bucketDLL = DLLContainer()

    for key in stream:
        if not key in seen:
            new_item = StreamItemNode(key, 1)
            seen[key] = new_item
            if 1 not in buckets:
                buckets[1] = BucketNode(1)
                bucketDLL.insert_node(buckets[1])
            buckets[1].item_list.insert_node(new_item)
        else:
            node = seen[key]
            new_count = node.count + 1
            old_count = node.count
            buckets[old_count].item_list.remove_node(node)
            if new_count not in buckets:
                bucket_node = BucketNode(new_count)
                buckets[new_count] = bucket_node
                bucketDLL.insert_before(bucket_node, buckets[old_count])

            
            if buckets[old_count].item_list.len == 0:
                bucketDLL.remove_node(buckets[old_count])
                del buckets[old_count]
            buckets[new_count].item_list.insert_node(node)
            node.count = new_count

        items = 0
        result = []
        start = bucketDLL.head
        while start.next and items < k:
            start = start.next
            if start.sentinel:
                break
            start_item = start.item_list.head
            while start_item.next and items < k:
                start_item = start_item.next
                if start_item.sentinel:
                    break
                result.append(start_item.key)
                items+=1
        yield result 





            


            

            



        


        

        




