'''
war story - psychic lottery numbers
'''

def generate_subsets_bit_shift(s):
    result = []
    for i in range(1 << len(s)):
        result.append([s[j] for j in range(len(s)) if (i & (1 << j))])
    return result

#res = generate_subsets_bit_shift([1,2,3])


def generate_subsets_iterative(s):
    res = [[]]
    for item in s:
        tmp = []
        for ss in res:
            tmp.append(ss + [item])
        res += tmp
    return res

#print(generate_subsets_iterative([1,2,3]))


def generate_subsets_recursive(s):

    result = []
    def generate(s, i, cur):
        if i == len(s):
            result.append(cur)
            return
        generate(s, i + 1, cur)
        generate(s, i+1, cur+[s[i]])


    generate(s, 0, [])
    return result

#print(generate_subsets_recursive([1,2,3]))


def subsets_binary_counting(s):
    result = []
