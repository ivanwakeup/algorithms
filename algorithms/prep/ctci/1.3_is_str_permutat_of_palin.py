'''
need to check if a string is a permutation of a palindrome

examples:
"baa" = yes
"aabb" = yes
"aabab" = yes

if strlen is even, all characters must appear even number of times
if strlen is odd, all chars must appear even num of times except 1

approaches:
1. could sort the string, and keep track of the number of times an odd character appears
2. could use a set, adding/removing as we traverse the string and ensure the set only contains 1 character if strlen is odd, or none if even

'''

def is_palindrome_permutation(s):

    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
        else:
            seen.remove(char)
    return len(seen) <= 1


print(is_palindrome_permutation("tact coa"))