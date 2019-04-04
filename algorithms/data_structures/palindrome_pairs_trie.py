def build_trie(trie_start, word, word_idx):
    for i in range(len(word)):
        if word[i] in trie_start:
            trie_start[word[i]][1].append(word_idx)
            trie_start[word[i]][2].append(i)
        else:
            trie_start[word[i]] = ({}, [word_idx], [i])
        trie_start = trie_start[word[i]][0]
    trie_start["*"] = None


# data = ["abcd","dcba","lls","les", "s","sssll"]
#
# trie = {}
#
# for i in range(len(data)):
#     build_trie(trie, data[i][::-1], i)
#
# print(trie)



'''
standard trie
'''

class Trie:

    paths = {}

    def __init__(self):
        pass

    def add_word(self, word):
        cur_path = self.paths
        for char in word:
            if char not in cur_path:
                cur_path[char] = {}
            cur_path = cur_path[char]
        cur_path["*"] = {}

    def has_word(self, word):
        prefix_trie = self.get_prefix_trie(word)
        if not prefix_trie:
            return False
        if "*" in prefix_trie:
            return True
        return False

    def has_prefix(self, prefix):
        pt = self.get_prefix_trie(prefix)
        if not pt:
            return False
        return True

    def get_prefix_trie(self, prefix):
        cur_path = self.paths
        for char in prefix:
            if char not in cur_path:
                return None
            cur_path = cur_path[char]
        return cur_path



# t = Trie()
# t.add_word("this")
# t.add_word("that")
# t.add_word("thisa")
# t.add_word("thisaa")
#
# print(t.has_word("thisaaa"))


'''
a trie used to solve the "palindrome pairs" problem. in addition to storing an array of words
as nested paths, we also store whether WORD(i, j) is a palindrome. that is, whether the word from index i to index j is palindromic

this class should be initialized with an array of words to store in the trie.
'''
from collections import defaultdict
class PPTrie:

    def __init__(self):
        self.paths = defaultdict(PPTrie)
        self.is_word_idx = -1
        self.palins_below = []

    @staticmethod
    def add_word(trie, word, idx):
        word = word[::-1]
        for i, char in enumerate(word):
            rev = word[::-1]
            is_palin_below = PPTrie.is_palindrome(rev[0:len(word)-i])
            if is_palin_below:
                trie.palins_below.append(idx)
            trie = trie.paths[char]
        trie.is_word_idx = idx

    @staticmethod
    def is_palindrome(word):
        if len(word) == 0 or len(word) == 1:
            return True
        return word[0] == word[-1] and PPTrie.is_palindrome(word[1:-1])

def build_trie(words):
    top_trie = PPTrie()
    for i, word in enumerate(words):
        PPTrie.add_word(top_trie, word,i)
    return top_trie



'''
search for each word in the trie.
if we encounter trie.is_word_idx, check if the remainder of the current word is a palindrome. if so, append its index as well as the is_word_idx to the result
additionally, append pairs of cur_word_idx and palins_below[i] for each i in palins_below

'''
def get_word_palins(trie, word):
    result = []
    for i, char in enumerate(word):
        #handling the case for the "" character. it would "form a word" at the root
        if trie.is_word_idx >= 0:
            if PPTrie.is_palindrome(word[0:len(word)-i]):
                result.append(trie.is_word_idx)
        if char not in trie.paths:
            return result
        trie = trie.paths[char]
    if trie.is_word_idx >= 0:
        result.append(trie.is_word_idx)
    result.extend(trie.palins_below)
    return result

def palindrome_pairs(words):

    pt = build_trie(words)
    result = []
    for i, word in enumerate(words):
        palins = get_word_palins(pt, word)
        for idx in palins:
            if idx != i:
                result.append([i, idx])
    return result


print(palindrome_pairs(["abcd","dcba","lls","s","sssll"]))