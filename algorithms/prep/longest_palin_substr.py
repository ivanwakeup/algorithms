def is_palindrome(s):
    mid = (len(s) - 1) // 2
    low = mid - 1
    high = mid + 1
    if len(s) % 2 == 0:
        if not s[mid] == s[mid + 1]:
            return False
        high += 1

    while low >= 0 and high < len(s):
        if not s[low] == s[high]:
            return False
        else:
            low -= 1
            high += 1

    return True


def brute_force_lps(s):

    if not s:
        return ""

    if len(s) < 3:
        return 2 if len(s) == 2 and s[0] == s[1] else 1

    longest = 1

    for i in range(1, len(s)+1):
        print("begin length {} strings".format(i))
        for j in range(len(s)-i+1):
            k = i + j - 1
            print("checking slice {}:{}".format(j, k))
            if is_palindrome(s[j:k+1]):
                longest = max(longest, len(s[j:k+1]))
    return longest


print(brute_force_lps("babab"))


#the rules for a string being a palindromic substring are:
#if Ssubi and Ssubj are equal, check middle string is also a palindrome
#for length 2 substrings, they are palindrome if s[i] == s[i+1]
#for length 3 and aboce,
def dp_lps(s):

    if not s:
        return 0

    dp = [[False]]