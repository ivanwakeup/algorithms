class Solution:
    def palindromePairs(self, words):
        trie = makeTrie(words)
        output = []
        for i, word in enumerate(words):
            candidates = self.getPalindromesForWord(trie, word)
            # this is how we don't add duplicates to result
            output.extend([[i, c] for c in candidates if i != c])
        return output

    def getPalindromesForWord(self, trie, word):

        output = []
        while word:
            if trie.wordEndIndex >= 0:
                if isPalindrome(word):
                    output.append(trie.wordEndIndex)
            if not word[0] in trie.paths:
                return output
            trie = trie.paths[word[0]]
            word = word[1:]

        if trie.wordEndIndex >= 0:
            output.append(trie.wordEndIndex)
        output.extend(trie.palindromesBelow)
        return output


from collections import defaultdict


class Trie:
    def __init__(self):
        # letter -> next trie node.
        self.paths = defaultdict(Trie)
        # If a word ends at this node, then this will be a positive value
        # that indicates the location of the word in the input list.
        self.wordEndIndex = -1
        # Stores all words that are palindromes from this node to end of word.
        # e.g. if we are on a path 'a','c' and word "babca" exists in this trie
        # (words are added in reverse), then "acbab"'s index will be in this
        # list since "bab" is a palindrome.
        self.palindromesBelow = []

    # Adds a word to the trie - the word will be added in
    # reverse (e.g. adding abcd adds the path d,c,b,a,$index) to the trie.
    # word - string the word to be added
    # index - int index of the word in the list, used as word identifier.
    def addWord(self, word, index):
        trie = self
        for j, char in enumerate(reversed(word)):
            if isPalindrome(word[0:len(word) - j]):
                trie.palindromesBelow.append(index)
            trie = trie.paths[char]
        trie.wordEndIndex = index


def makeTrie(words):
    trie = Trie()
    for i, word in enumerate(words):
        trie.addWord(word, i)
    return trie


def isPalindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    return word[0] == word[-1] and isPalindrome(word[1:-1])


sol = Solution()

sol.palindromePairs(["abcd","dcba","lls","s","sssll"])