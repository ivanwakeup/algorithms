#brute force compares each element i with all of the other elements and keeps track of the max sum along the way
#return the subarray with the maximum sum


def max_sub_1(arr):
    max_sum = -9999

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            max_sum = max(max_sum, sum(arr[i:j+1]))
    return max_sum



def max_sub_2(arr):

    def crossover_sum(arr, l, m, h):
        left_sum = -9999
        sum=0
        left_low=m
        for i in range(m,l-1, -1):
            sum = sum + arr[i]
            if sum >= left_sum:
                left_low = i
                left_sum = sum
        right_sum = -9999
        sum=0
        right_high=m
        for j in range(m+1, h+1):
            sum = sum + arr[j]
            if sum >= right_sum:
                right_high = j
                right_sum = sum

        return (left_sum+right_sum, left_low, right_high)

    def max_sum_sub(arr, low, high):
        if low == high:
            return (arr[low], low, high)
        mid = (high+low)//2

        left_sum, left_low, left_high = max_sum_sub(arr, low, mid)
        right_sum, right_low, right_high = max_sum_sub(arr, mid+1, high)
        cross_sum, cross_low, cross_high = crossover_sum(arr, low, mid, high)

        if left_sum < cross_sum and cross_sum > right_sum:
            return (cross_sum, cross_low, cross_high)
        elif left_sum >= cross_sum and left_sum > right_sum:
            return (left_sum, left_low, left_high)
        else:
            return (right_sum, right_low, right_high)

    total = max_sum_sub(arr, 0, len(arr)-1)
    return total[0]


data = [-3,-6,-1]

print(max_sub_2(data))