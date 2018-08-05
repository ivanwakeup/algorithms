def lengthOfLongestSubstring(s):
    ans = 0
    length = len(s)

    for i in range(0, length):
        for k in range(i+1, length+1):
            if allUnique(s, i, k):
                ans = max(ans, k -i)
    return ans


def allUnique(str, start, stop):
    tmp = set()
    for i in range(start, stop):
        if str[i] in tmp:
            return False
        tmp.add(str[i])
    return True



print(lengthOfLongestSubstring("dvdz"))



#you can take the end idx subtract the start idx of a string to find its length, this is used here to determine what the actual length of the substr is

#if there are pieces of the algorithm you can split out, do it!

