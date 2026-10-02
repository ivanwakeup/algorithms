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
            median = (max_h[0] + min_h[0]) // 2
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


for item in top_k_elements_indexed_pq(RandomNumberStream(1, 100), 3):
    print(item)




