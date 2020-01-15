'''

the number of subsets of arr =

num subsets of arr[i] + num
'''


def get_subsets(arr):

    subset = []
    def generate_subsets(arr, i, cur_path):
        if i == len(arr):
            subset.append(cur_path)
            return

        generate_subsets(arr, i+1, cur_path+[arr[i]])
        generate_subsets(arr, i+1, cur_path)

        return

    generate_subsets(arr, 0, [])

    return subset


'''
num_subsets(arr, i) = num subsets of some arrays_and_strings from position i

num_subsets(arr, i) = num_subsets(arr, i+1)
'''
# print(get_subsets([1,2,3,4]))


def get_num_subsets(arr, i):
    if i == len(arr) - 1:
        return 1

    return get_num_subsets(arr, i) + get_num_subsets(arr, i + 1)


print(get_num_subsets([1,2,3,4], 0))


