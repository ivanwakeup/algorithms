'''
String Rotation: Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one
call to i5Sub5tring (e.g., "waterbottle" is a rotation of" erbottlewat").
'''

'''
substr method:
s1 in s2
'''

'''
examples:

"hist" rotation of "this"? yes

rotation: s2 is a rotation of s1 if after slicing off the first char of s2 and appending it to the end some number of times, s1 can be formed.

idea:

traverse s1 until s1[i] matches the first character of s2
keep track of letters seen up to that point
then check if s2[0:len(tmp)] in s1 (this is the call to isSubstr)
then check if the end of the s2 string matches the beginning of the s1 string


what is the runtime here?

0(s) where s is the length of the string, if the lengths aren't equal we immediately return False

how could we improve?
not sure
'''

def is_rotation_1_call(s1, s2):
    if len(s1) != len(s2):
        return False
    i = 0
    tmp = []
    while s1[i] != s2[0]:
        tmp.append(s1[i])
        i += 1
    tmp = "".join(tmp)

    if not s2[0:len(s2)-len(tmp)] in s1:
        return False
    j = 0
    while i:
        if s1[j] != s2[len(s2)-i]:
            return False
        i-=1
        j+=1
    return True


#print(is_rotation_1_call("waterbottle", "erbottlewat"))


'''
you can actually do this by realizing the following:

if s2 is a rotation of s1, then:

s1 == some beginning substr X and some ending substring Y
so, s1 == XY

if s2 is a rotation, then, s2 would just be:

s2 == YX

where Y was that ending portion for s1 and X was the beginning portion.
if it can't be expressed this way, it must not be a substring!!!


with that in mind.....you could just append s1 to itself to get:

s1s1 == XYXY

YX is the middle substring! now just check if s2 in s1s1!!


'''

def is_substr_clever(s1, s2):
    if len(s1) != len(s2):
        return False

    s1s1 = s1 + s1
    return s2 in s1s1


print(is_substr_clever("waterbottle", "erbottlewat"))