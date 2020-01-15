import random
def partition(arr, lo, hi):
    piv = random.randint(lo, hi)
    print("using pivot {}".format(piv))
    arr[piv],arr[hi] = arr[hi],arr[piv]
    i = lo-1
    j = lo
    while j < hi:
        if arr[j] < arr[hi]:
            i+=1
            arr[j], arr[i] = arr[i], arr[j]
        j+=1
    arr[hi], arr[i+1] = arr[i+1], arr[hi]


data = [4,7,3,1,9,8,5,0,1]
partition(data, 1, 4)
print(data)
    