'''
Given a hotel which has 10 floors [0-9] and each floor has 26 rooms [A-Z]. You are given a sequence of rooms,
where + suggests room is booked, - room is freed. You have to find which room is booked maximum number of times.

You may assume that the list describe a correct sequence of bookings in chronological order; that is, only free rooms
can be booked and only booked rooms can be freeed. All rooms are initially free.
Note that this does not mean that all rooms have to be free at the end. In case, 2 rooms have been booked the same number
of times, return the lexographically smaller room.

You may assume:

N (length of input) is an integer within the range [1, 600]
each element of arrays_and_strings A is a string consisting of three characters: "+" or "-"; a digit "0"-"9"; and uppercase English letter "A" - "Z"
the sequence is correct. That is every booked room was previously free and every freed room was previously booked.
Example:

Input: ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]
Output: "1A"
Explanation: 1A as it has been booked 2 times.


1. find a brute force!
can't we just hashmap it and count whichever room is booked the most?

plan:
iterate over input, parse the roomnum/floor

add it to hashmap

then iterate over hashmap keys, keeping track of highest room count
if we encounter a key with the same room count, update the result to that key
if its lexicographic order is lower than the prev


alternative solution:
sort the list lexicographically in 0(nlogn) time
use a sliding window approach to keep track of the largest booked size
'''


from collections import defaultdict
def most_booked_room(rooms):
    hm = defaultdict(int)
    for room in rooms:
        if room[0] == "+":
            hm[room[1:]]+=1

    res = 0
    rkey = None
    for key in hm.keys():
        if hm[key] > res:
            rkey = key
            res = hm[key]
        elif hm[key] == res and key<rkey:
            rkey = key
            res = hm[key]
    return rkey

data = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E", "+3E", "-3E", "+3E"]


def most_booked_sorted_approach(rooms):
    rooms.sort()
    i = 0
    best_count = 0
    best_key = None
    while i < len(rooms):
        if rooms[i][0] == "-":
            i+=1
            continue
        j = i
        cnt = 0
        while j < len(rooms) and rooms[j] == rooms[i]:
            cnt+=1
            j+=1
        if cnt >= best_count:
            if cnt == best_count:
                best_key = rooms[i][1:] if rooms[i][1:] < best_key else best_key
            elif cnt > best_count:
                best_key = rooms[i][1:]
                best_count = cnt
        i = j
    return best_key

print(most_booked_sorted_approach(data))