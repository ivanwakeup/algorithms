'''
(1, 5) | (2, 6) -> (1, 6)
(2, 10) | (1, 2) -> (2, 10)
(1, 3) | (2, 6) | (7, 10) -> (1, 6) | (7, 10)
(7, 8) | (2, 6) | (1, 100)

(1, 3) | (2, 6) | (5, 8) | (7, 7) | (9, 12)
sort them by start time, end time doesnt work. why? because something with a high end time but low start time might wind up later in the sorted version and previous things
that should've gotten merged into it are missed. sort by start time guarantees we merge everything that shoudl be merged as we process.
'''

def merge_intervals(intervals):

    def overlaps(i1, i2):
        return i2[0] <= i1[1]

    if len(intervals) == 1 or len(intervals) == 0:
        return intervals

    s_intervals = list(sorted(intervals, key=lambda x: x[0]))
    result = []
    prev = s_intervals[0]
    i = 1
    while i < len(s_intervals):
        if overlaps(prev, s_intervals[i]):
            prev = [min(prev[0], s_intervals[i][0]), max(prev[1], s_intervals[i][1])]
        else:
            result.append(prev)
            prev = s_intervals[i]
        i+=1
    result.append(prev)
    return result

from dataclasses import dataclass

@dataclass
class Interval:
    start: int
    end: int

def overlaps(i1, i2):
    #i1 is the earlier starting interval
    if i1.start <= i2.start:
        return i2.start <= i1.end
    #its the later starting interval
    else:
        return i1.start <= i2.end

def merge_interval(i1, i2):
    return Interval(start=min(i1.start, i2.start), end=max(i1.end, i2.end))
    
'''
we find the insertion point
'''
def insert_intervals(intervals, n_interval):
    
    result = []
    i=0

    #all intervals that definitely dont overlap
    while i < len(intervals) and intervals[i].end < n_interval.start:
        result.append(intervals[i])
        i+=1

    #maybe now we overlap
    merged = n_interval
    while i < len(intervals) and overlaps(merged, intervals[i]):
        merged = merge_interval(merged, intervals[i])
        i+=1
    result.append(merged)

    result.extend(intervals[i:])
    

    return result

        

