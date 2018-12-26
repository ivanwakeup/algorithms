'''
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
->
spale, pale ->
pale, bale ->
pale, bake ->
pale,
ple
true
true
true
false
Hints:#23, #97, #130


examples:

abab, abac -> True, replace a char
aba, abac -> True, insert a char in s1 or delete a char in s2
bbcab, bb -> False, strings differ in length by at least 2
"", "a" -> True, insert or replace char

"spale", "pale" -> True


observations:
1. if str lengths differ by more than 1, return false

else:
keep track of difference count and iterate over the string

brute force?:
maintain pointers at beginning of each string
if you find a difference, move the pointer for the string you find the difference in forward
if difference ever is above 1, return False

What if you get to the end of the string and theres chars left?
just return if remaining + diff <= 1!
'''

def is_one_edit(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    i = 0
    j = 0
    diffs = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            diffs += 1
            if diffs > 1:
                return False
            #move the pointer in the longer string forward!
            if len(s1) == len(s2):
                i+=1
                j+=1
            elif len(s1) > len(s2):
                i+=1
            else:
                j+=1
        else:
            i+=1
            j+=1

    return (diffs + (len(s1)-i) + (len(s2)-j) <= 1)

print(is_one_edit("apple", "aple"))

'''
what is runtime?
O(s) where s is the shorter string
'''