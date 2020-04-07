'''
let's implement a trie like the one for our lyft interview.

at each node we'll store:
1. what words exist below this word
'''


class TrieNode:

    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.is_word = False
        self.words_below = []

    def __eq__(self, other):
        return self.value == other

    def __repr__(self):
        return f"{self.value}->{self.children}"


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def __repr__(self):
        return self.root.__repr__()

    def add_word(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
            curr.words_below.append(word)
        curr.is_word = True

    def has_word(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_word

    def get_words_for_prefix(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        return curr.words_below



t = Trie()
t.add_word("this")
t.add_word("that")
t.add_word("those")
t.add_word("hello")
t.add_word("hell")

print(
    t.has_word("hell")
)