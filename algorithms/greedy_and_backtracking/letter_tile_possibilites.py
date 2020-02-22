'''
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.



Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188


INTUITION
1. there are some sequences that will be repeated, so if we can build the path in some
order that avoids reconsidering sequences that we've already built, then we don't have to build
EVERY permutation of EVERY possible 
'''

def numTilePossibilities(tiles):
    result = set()

    def dfs(arr, path):
        # this is the "backtracking" part. if we've already started
        # to build a path that contains a prefix we've seen before,
        # we KNOW we've already built anything else that path can contain
        # because we would've encountered it on an earlier DFS.
        if path in result:
            return
        if path:
            print(path)
            result.add(path)
        nxt = list(arr)[:]
        for j in range(len(nxt)):
            nxtpath = path + nxt[j]
            pas = nxt[:j] + nxt[j+1:]
            dfs("".join(pas), nxtpath)

    dfs(tiles, "")
    return len(result)

print(numTilePossibilities("AAABDLAHDFBC"))