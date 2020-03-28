'''
brute force:
keep extra array states of length n
iterate over input, "turn on" the light at states[light[k]]
once the light is turned on, traverse the states array and do:
    -if the prev states[k-1] is on and it is blue, turn the current light blue
    -else leave it just "on"
    -increment result if all the lights on the traversal are blue


intutions on linear runtime:

let M = a moment where all lightbulbs which are turned on are blue

for M to be true, all lightbulbs prior to our HIGHEST ILLUMINATED LIGHT need to be on.

how can we check if they are on?
1. an easy way to think about it is just to keep track of how many light bulbs we've turned on already.
if LIGHTS_TURNED_ON = HIGHEST_LIGHT_ON then all of our lightbulbs must be blue.

2. we can also think about it by the sum of the series prior to the currently turned on light!

for M to be true in this case, when we are considering lightbulb I (by position, not by index),
the cur_sum we've seen so far needs to MATCH the sum we expect to see. The sum we expect to see is
simply the sum of the series 1 to N.


the two optimal approaches are highlighted below!

'''
class Solution:
    def numTimesAllBlue(self, light):
        highest = 0
        num_on = 0
        res = 0
        for l in light:
            highest = max(highest, l)
            num_on+=1
            if num_on == highest:
                res+=1
        return res


class Solution:
    def numTimesAllBlue_series_summation(self, light) :
        target = 0
        cur_sum = 0
        result = 0
        for i in range(1, len(light) + 1):
            cur_sum += light[i - 1]
            target += i
            if target == cur_sum:
                result += 1
        return result
