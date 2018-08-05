def words(s):
    j = 0
    result = []
    for i in range(len(s)):
        if s[i] == " " or i == len(s) - 1:
            if not s[j] == " " or not s[i] == " ":
                result.append(s[j:i])
            j = i + 1

    return len(result)

print(words("    sssdf  fdf    "))
