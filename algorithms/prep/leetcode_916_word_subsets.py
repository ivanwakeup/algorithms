def wordSubsets(A, B):
    result = []
    universal_count = len(B)

    for word in A:
        curr = 0
        cur_uni = 0
        start = 0
        done = len(B[start])
        for char in word:
            if start >= len(B):
                break
            if char in B[start]:
                curr += 1
                if curr == done:
                    curr = 0
                    cur_uni += 1
                    start += 1
                    if start >= len(B):
                        break
                    done = len(B[start])
        if cur_uni >= universal_count:
            result.append(word)

    return result


A = ["amazon","apple","facebook","google","leetcode"]
B = ["e","o"]


print(wordSubsets(A, B))