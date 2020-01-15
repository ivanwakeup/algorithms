'''
wow this one is like fucking mind boggling.

INTUITION:
we can use a "base" subset as the start for adding the next element we're considering
to everything that already exists.

for example, if we start with the empty subset {}:
how many subsets can we make once we add the element 1? Well, just two:
{}
and
{1}

now when we have those two subsets, we can add any ADDITIONAL element to any existing subsets we have to form
all of the possible subsets with that additional element. So, add 2 and we have:
{}
{1}
{2}
{1,2}

we can continue on like this to create every possible subset for further elements we want to add.
'''
def subsets(nums):
    result = [[]]
    for num in nums:
        tmp = result.copy()
        for item in result:
            tmp.append([num] + item)
        result = tmp
    return result


data = [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
#print(subsets([1,2,3]))


'''
we can also define this recursively
'''

def subsets_recursive(nums):
    result = []
    def dfs(path, nums):
        result.append(path)
        if not nums:
            return
        for i, num in enumerate(nums):
            dfs(path+[num], nums[i+1:])
    dfs([], nums)
    return result

print(subsets_recursive([1,2,3]))