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
class PPTrie:

    paths = {}

    def __init__(self, input_words):
        for idx, word in enumerate(input_words):
            self.add_word(word, idx)

    def add_word(self, word, idx):
        pass

    def is_palindrome(self, word, i, j):
        while i < j:
            if word[i] != word[j]:
                return False
            i+=1
            j-=1
        return True