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