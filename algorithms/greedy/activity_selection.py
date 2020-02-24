'''

given N activities with their start and finish times, determine the maximum number of activities that can be performed
by one person.

ex:
input[i][0] = start time
input[i][1] = end time

activities:
[[1,5], [2, 3], [4,5], [6, 8]]
we could do 3 activities[i] => [2,3] [4,5] and [6,8]



approach ideas:
1. we could just greedily try and choose the shortest duration activity that starts after our current end time on each
iteration. would need n^2 runtime to do it

CAN WE DO BETTER?
we could sort the input by ending times, and just take the activity that ends first! we are trying to maximize our
activities so it makes sense to just commit to whatever ends first.
'''


def activity_select(activities):
    activities.sort(key=lambda x: x[1])
    cnt = 0
    prev = None
    for activity in activities:
        if not prev:
            cnt+=1
            prev = activity
            continue
        if activity[0] >= prev[1]:
            cnt+=1
            prev = activity

    return cnt


print(activity_select([[1,2], [1,5], [2, 3], [4,5], [6, 8]]))

