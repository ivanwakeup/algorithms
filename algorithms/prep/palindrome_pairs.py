'''

edge cases:
1. need to check in TRIE that the word we're trying to find isn't the same index as the one we're currently considering
2. once we find the PREFIX for a string in the TRIE:
    1. it may have multiple suffixes, need to check if any of them are palindromes. so:
        for each LETTER in the next level of the trie, check if the string INDEXED by that trie is a palindrome between
        the index that LETTER appears at and the start of the string.

    2. we may have found a potential SUFFIX in the array, rather than a prefix. if this is the case,
        we need to check that the remainder of the string we're checking is also a palindrome.


what to store in TrieNode:
(letter, word_idx_array, char_idx_array)


approach:
add reverse of each word to Trie, storing (letter, word_idx_array, char_idx_array)
iterate through WORDS. For each CHAR in WORD:
    if CHAR in TRIE:
        store index I of CHAR
        keep finding CHAR in TRIE if it exists. if it doesnt, we can't form a palindrome pair so continue
        if we reach the end of the WORD, for each word in TRIE[WORD_IDX_ARRAY], can we form palindrome between word start and CHAR_IDX_ARRAY-1?
        if we don't reach end of WORD, did we find a * in trie and the rest of WORD is palindrome?

'''
class Solution(object):
    def palindromePairs(self, words):
        top_trie = {}
        for i in range(len(words)):
            self.build_trie(top_trie, words[i][::-1], i)
        result = []
        for s in range(len(words)):
            trie = top_trie
            word = words[s]
            for i in range(len(word)):
                if not word[i] in trie:
                    break

                #need to make sure the index of this letter in the trie ISNT THE SAME as the one we're checking
                if len(trie[word[i]][1])==1 and trie[word[i]][1][0] == s:
                    break

                if i == len(word)-1:
                    for j, idx in enumerate(trie[word[i]][1]):
                        to_check = words[idx]
                        start = trie[word[i]][2][j]
                        if self.is_palindromic(to_check, 0, start):
                            result.append([s, idx])
                            break

                trie = trie[word[i]][0]
                if "*" in trie and trie["*"][1][0] != s:
                    if self.is_palindromic(word, i+1, len(word)-1):
                        idx = trie["*"][1][0]
                        result.append([s, idx])

        return result


    '''
    is the string palindromic between two indicies?
    '''
    def is_palindromic(self, s, l, h):
        if not s:
            return True
        while l < h:
            if s[l] != s[h]:
                return False
            l+=1
            h-=1
        return True

    def build_trie(self, trie_start, word, word_idx):
        for i in range(len(word)):
            if word[i] in trie_start:
                trie_start[word[i]][1].append(word_idx)
                trie_start[word[i]][2].append(i)
            else:
                trie_start[word[i]] = ({}, [word_idx], [i])
            trie_start = trie_start[word[i]][0]
        trie_start["*"] = (None, [word_idx], -1)



sol = Solution()

print(sol.palindromePairs(["lls","s","sssll"]))
