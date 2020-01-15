'''
check if a string is a permutation of another

s1 = "abba"
s2 = "bbaa"
= YES

if str lenghts are different, then no

approaches:
sort both strings, ensure characters appear at the same indicies (overal nlogn)
add str1 and character counts to hashmap, iterate over second string and subtract char coutns from hashmap, ensure all coutns are 0 at the end. (space complexity = 0(n)) linear time

use simple arrays_and_strings of 26 characters (should we assume only alphabetic chars? maybe input is everything in ASCII range? at the end, check that arrays_and_strings has no 1 values!
'''

def is_permutation(s1, s2):

    flags = [0] * 128
    chk_str = s1 + s2
    for char in chk_str:
        i = ord(char)
        flags[i] = flags[i] ^ 1
    for char in flags:
        if char:
            return False
    return True


def is_permutation_bit_vector(s1, s2):

    flags = 0
    chk_str = s1 + s2
    for char in chk_str:
        i = ord(char)
        flags = flags ^ (1<<i)

    return not flags

print(is_permutation_bit_vector("thiss", "ssthi"))
