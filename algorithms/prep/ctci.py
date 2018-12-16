'''


'''

def unique_chars(s):
    contains = [False for _ in range(0, ord('z')+1)]
    for char in s:
        if contains[ord(char.lower())]:
            return False
        contains[ord(char.lower())] = True
    return True

#print(unique_chars("thit"))


def is_permutation(s1, s2):
    from collections import defaultdict
    d = defaultdict(int)
    for char in s1:
        d[char] += 1
    for char in s2:
        if char in d:
            d[char] -= 1
        else:
            return False

    for char in d.keys():
        if d[char] != 0:
            return False

    return True

#print(is_permutation("tffhigfsgf", "shitffgff"))


#a bit vector is basically an array of True/False. Don't get hung up on the int value of CHECKER here
#what we care about is the binary representation of checker (in other words, the array of bits that is has)
#this algorithm works by setting bits with: checker |= (1 << val). this has the effect of setting the 'val'th bit to 1
def is_unique_bit_vector(s):
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        #if the 'val'th bit is on, we have a dupe. but why?
        if(checker & (1 << val)):
            return False
        checker |= (1 << val)
    return True

#print(is_unique_bit_vector("tht"))


'''
XOR each number with the previous result to get your answer
remember, XOR returns 0 if the numbers are the same

Why does this work?

XOR has two properties that help higlight this:
Y ^ 0 = Y

X ^ X ^ Y = Y  IS EQUIVALENT TO (X ^ 0) ^ (X ^ 0) ^ Y = Y

because the order of operations doesn't matter, any time you take some number Y and XOR it with some other set of numbers
that XOR to 0, you'll always get Y back.

"remember, XOR returns 0 if nums are the same:
so:
Y ^ 0 = Y
just flip the equation to see this:
Y ^ Y = 0
'''
def find_element_that_occurs_odd_num_times(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result ^= arr[i]
    return result


#print(find_element_that_occurs_odd_num_times([1,7,1,7,7,4,4]))


def approximate_log_base_2(num):
    result = 0
    while num > 2:
        num = num >> 1
        result += 1
    return result

print(calc_log_base_2(45353))
