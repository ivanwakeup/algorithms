'''
given a string that represents a message to an internet forum, and a limit of length K,

crop the input string such that:
1. the message isn't longer than K
2. the cropping doesn't crop part of a word
3. the cropping doesn't end with a space
4. the output should be as long as possible

examples:
"this", k=5
ans = "", we don't have enough characters to fit ANYTHING

"this is fun", k=10
ans = "this is", we can't fit all of fun so we return as many words as we can

"wow                ", k=5
ans = "wow", trim the white space from the end of the string



plan:
traverse the input, and every time we form a word add it to a result array
keep track of length along the way
once we hit k, just return the space separated result array
'''


def crop_words(message, k):
    result = []
    buf = []
    for i, char in enumerate(message):
        if char == " " and buf:
            result.append("".join(buf))
            buf = []
        if i >= k:
            return " ".join(result) if result else ""
        elif char != " ":
            buf.append(char)

    if buf:
        result.append("".join(buf))

    return " ".join(result) if result else ""

'''
an optimized solution would be to 
1. return the base case of K>= len(input) then just return the input
immediately slice the input at K+1
if our message[K] != " ", we must've sliced in the middle of a word somewhere
so move k backwards and delete from the input string until we find " " or k < 0, at which point we've
found the point to return the string up to
'''

def crop_words_optimized(message, k):
    if k >= len(message):
        return message
    sliced = message[:k+1]
    while message[k] != " " and k > 0:
        k-=1
    return sliced[:k].strip()

datas = [
    ("this is fun", 10, "this is"),
    ("wow          ", 5, "wow"),
    ("this", 5, "this"),
    ("Codility We Test Coders", 14, "Codility We"),
    ("fun times", 0, ""),
    ("fun times", 2, ""),
    ("fun times", 3, "fun"),
    ("Codility We Test Coders", 16, "Codility We Test"),
    ("Codility We Test Coders", 15, "Codility We"),
    ("Codility We Test Coders", 200, "Codility We Test Coders")
]

for data in datas:
    try:
        assert(crop_words_optimized(data[0], data[1]) == data[2])
        print(f"assertion passed!! \"{data[0]}\" at {data[1]} == \"{data[2]}\"")
    except AssertionError:
        print(f"assertion failed for \"{data[0]}\" at {data[1]}")