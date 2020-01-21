'''

we don't even need to maintain a sorted partition. basically just consdier, starting from index 1
whether the current index is smaller than the one before it.

WHILE it is smaller,
swap it with the one before it.
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
