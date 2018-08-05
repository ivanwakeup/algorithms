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


def letterCombinations( digits):
    result = []
    for i in range(len(digits)):
        letters = mapping[int(digits[i])]
        for letter in letters:
            result.append([letter])
    return result


print(letterCombinations("23"))