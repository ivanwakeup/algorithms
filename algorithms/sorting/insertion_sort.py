'''

intuitions:
1. everything up to arr[i] is sorted
2. when considering arr[i], it may be not in sorted position
3. therefore, we need to scan backwards through the array and swap
'''

def insertion_sort(arr):

    for i in range(1, len(arr)):
        j = i
        while j and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1


data = [7,4,1,9,3,2,1]

insertion_sort(data)

print(data)
