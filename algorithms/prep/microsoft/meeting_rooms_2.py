'''
given an array of intervals that represent meeting start and end times, find the min number of meeting rooms
required to serve all the meetings.

ex:
[(0, 30), (5, 10), (15, 20)]
ans = 2, (5,10) and (15, 20) could go in the same meeting room because they don't overlap

[(0,4), (3,7), (5, 8)]
ans = 2, (0,4) and (3,7) overlap so they need 2 meeting rooms, but (5,8) could go in the meeting
room that (0,4) was held in


intuitions:
if the first two meetings we process overlap, we definitely need at least 2 meeting rooms

what about the THIRD meeting room?
we might be able to get away with 2 meeting rooms, if it only overlaps ONE of the previous two overlapping
if it overlaps both, we need a THIRD meeting room.

what about the nth meeting room?
so long as there is at least 1 meeting room that it DOESNT overlap with, we can use one of those meeting rooms.

Which room would it NOT overlap with?
if we are processing the meeting rooms by their start time, we could find the meeting that ended with the oldest
end time. if the nth interval doesn't overlap with that, we don't need an additional meeting room.

BUT, then we must merge this interval and the interval it doesn't overlap with, updating its end time accordingly.


plan:
sort input by start time
determine if the current interval overlaps with the interval at the top of a min_heap ordered by END_TIME
if it does, increment our result by one and merge it with the interval at the top of the heap,
placing it back on the heap

runtime:
O(nlogn)
'''

def overlaps(i1, i2):
    return i2[0] <= i1[1]

def merge(i1, i2):
    return [min(i1[0], i2[0]), max(i1[1], i2[1])]

from queue import PriorityQueue
def get_num_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x[1])
    pq = PriorityQueue()
    if not meetings:
        return 0
    result = 1
    pq.put((meetings[0][1], meetings[0]))
    for i in range(1, len(meetings)):
        if overlaps(pq.queue[0][1], meetings[i]):
            node = pq.get()
            to_put = merge(node[1], meetings[i])
            pq.put((to_put[1], to_put))
            result+=1
        else:
            pq.put((meetings[i][1], meetings[i]))
    return result


datas = [
    [(0, 30), (5, 10), (15, 20)],
    [(0,4), (3,7), (5, 8)]
]

for data in datas:
    print(
        get_num_meeting_rooms(data)
    )