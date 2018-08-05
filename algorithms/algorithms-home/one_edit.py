def is_one_edit(word1, word2):
    if abs(len(word1) - len(word2)) > 1:
        return False

    else:
        i, j = 0, 0
        diff = 0
        while i < len(word1) and j < len(word2):
            if word1[i] != word2[j]:
                diff += 1
                if len(word1) > len(word2):
                    i += 1
                elif len(word2) > len(word1):
                    j += 1
            else:
                i += 1
                j += 1
        if len(word1) > i or len(word2) > j:
            diff += 1
        return diff == 1


print(is_one_edit("this", "athis"))

