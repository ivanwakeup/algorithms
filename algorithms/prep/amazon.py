#solve maximize pairs problem
max_dist = 10000
forward = [
    [1, 1000],
    [2, 3000],
    [3, 4000],
    [4, 10000],
    [5, 9000],
    [6, 7000]
]
backward = [
    [1, 3000],
    [2, 5000],
    [3, 4000],
    [4, 1000]
]
#what pair of forward/backward maximizes the dist utilized without going over max_dist?
# return id pairs of trips that maximize

#n * m runtime n = len(forward) m = len(backward)
def brute_force(max_dist, forward, backward):
    best = 0
    f = forward
    b = backward
    result = []
    for i in range(len(forward)):
        for j in range(len(backward)):
            if f[i][1] + b[j][1] <= max_dist:
                best = max(best, f[i][1] + b[j][1])

    for i in range(len(forward)):
        for j in range(len(backward)):
            if f[i][1] + b[j][1] == max_dist:
                result.append([f[i][0], b[j][0]])

    return result


def sorted_optimized(max_dist, forward, backward):
    f = sorted(forward, key=lambda x: x[1])
    b = sorted(backward, key=lambda x: x[1])
    print(f)
    print(b)
    j = 0
    n = len(forward)
    result = []
    cur_max = 0
    for i in range(n):
        if j<n:
            if f[i][1] + b[j][1] <= max_dist:
                cur_max = max(cur_max, f[i][1] + b[j][1])
                j+=1
            elif f[i][1] > b[j][1]:
                j+=1
    return cur_max

#print(brute_force(max_dist, forward, backward))
print(sorted_optimized(max_dist,forward,backward))