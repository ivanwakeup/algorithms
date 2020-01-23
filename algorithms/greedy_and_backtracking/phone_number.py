'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want



intuition:
this is basically a pure backtracking problem
'''
mapping = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}

def letterCombinations(digits):
    res = []
    recurse("", digits, 0, res)
    return res


def recurse(prefix, digits, i, result):
    if i >= len(digits):
        result.append(prefix)
        return
    letters = mapping[int(digits[i])]
    for x in range(len(letters)):
        recurse(prefix + letters[x], digits, i + 1, result)


print(letterCombinations("23"))