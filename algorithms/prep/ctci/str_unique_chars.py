'''
want to use bit masking to determine if i've already seen a character before
my bit array will be 26 bits long and represent whether i've seen the current character already
'''
def str_unique_chars(s):
    bit_vector = 0
    for char in s:
        char_bit = ord(char) - ord('a')
        mask = (1 << char_bit)
        #have we seen this bit already?
        if bit_vector & mask:
            return False
        bit_vector |= mask
    return True

print(str_unique_chars("thih"))