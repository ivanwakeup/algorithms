'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).


"aaba" -> "a2ba"
"aaaaabbcca" -> "a5b2c2a"
"a" -> "a"
abc -> abc
abbbbbbbbbb -> "a""b""1""0"


algorithm:
start at the 0th index keeping track of char count. move a j pointer forward until j+1 != j (at this point we have the end of a compressed sequence)
update the i'th position (position under consideration) with the original char
if we have more than 1 of the j'th character, update the i+1 position to be the count[0] (keep slicing count to account for counts > 9) then move i forward

at the end of each iteration move j forward (will now point to the next new character)
and move i forward (maintains the position that needs to be updated)
'''


'''
return LENGTH of compressed string
'''
def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    if len(chars) == 1:
        return 1
    i = 0
    j = 0
    while j < len(chars):
        local = 1
        char = chars[j]
        while j + 1 < len(chars) and chars[j + 1] == chars[j]:
            local += 1
            j += 1
        #j will move forward, so make sure to update the current char under consideration
        chars[i] = char
        # i've hit a new char or the end of the array or both
        if local > 1:
            local = str(local)
            # handle local count having more than 1 digitg
            while local:
                chars[i + 1] = local[0]
                local = local[1:]
                i += 1
        #at the end, i will be the length of the compressed string
        i += 1
        j += 1
    return i