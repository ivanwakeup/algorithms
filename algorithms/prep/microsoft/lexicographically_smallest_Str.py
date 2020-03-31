'''
Lexicographically smallest string formed by removing at most one character.

Example 1:

Input: "abczd"
Output: "abcd"

"ddbfa" => "dbfa"
"abcd" => "abc"
"dcba" => "cba"
"dbca" => "bca"


approach:
just remove the first character that we find that appears later in the alphabet than the char after it.
'''

def lexicograph(s):
    arr = list(s)
    result = []
    removed=False
    for item in arr:
        if result and ord(result[-1]) >= ord(item) and not removed:
            result.pop()
            removed=True
        result.append(item)
    return "".join(result)

print(
    lexicograph("abczd")
)
