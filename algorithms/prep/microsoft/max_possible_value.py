'''
given an integer, return the maximum possible value achievable by inserting a '5'
somewhere in that integer.

examples:
240 => 5240, 5 at the front yields the max value
9999 => 99995, 5 at the end yields the best value
-9999 => -59999 at the front yields the best value
32330 => 532330, 5 at the front
6622 => 66522 yields the highest possible value
-111 => -1115
-6 => -56
-4 => -45
-116633 => -1156633
-454 =>
solution:
if the number is negative, the 5 goes directly before the first number that is greater than it
if the number is positive, the 5 goes directly after the last number that is greater than it
'''


def max_possible_value(value):
    vs = list(str(value))
    idx = 0
    if value < 0:
        for char in vs:
            if char == "-":
                idx+=1
                continue
            if int(char) > 5:
                break
            idx+=1
    else:
        for i, char in enumerate(vs):
            if int(char) > 5:
                idx = i+1
    vs.insert(idx, str(5))
    return int("".join(vs))

datas = [
    (240, 5240),
    (999, 9995),
    (-6, -56),
    (-5, -55),
    (-4, -45),
    (32330, 532330),
    (-116633, -1156633)
]

for data in datas:
    try:
        assert(max_possible_value(data[0]) == data[1])
        print(f"assertion succeeded for {data[0]} == {data[1]}")
    except AssertionError:
        print(f"assertion failed for for {data[0]} == {data[1]}")