'''
what does a trie do?
it is useful for looking up if a string exists in O(n) time, where n is the length of a string.

'''

class Trie:

    def __init__(self):
        self.root = None
        self.children = {}

    def has_prefix(self, pref):
        root, word = self.traverse_while_prefix(pref)
        if not word:
            return True
        return False

    def add_word(self, word):
        head = self.children
        chk_node = TrieNode('\0')
        while word and word[0] in self.children:
            dict = self.children[word[0]]
            self.children = dict
            word = word[1:]
        if not word:
            if chk_node in self.children:
                return
            else:
                self.children[chk_node] = chk_node.children
        else:
            while word:
                node = TrieNode(word[0])
                word = word[1:]
                self.children[node] = node.children
                self.children = self.children[node]
            self.children[chk_node] = chk_node.children
        self.children = head

    def has_word(self, word):
        root, word = self.traverse_while_prefix(word)
        if not word and '\0' in root:
            return True
        return False

    def traverse_while_prefix(self, word):
        root = self.children
        while word and word[0] in root:
            root = root[word[0]]
            word = word[1:]
        return root, word



class TrieNode:
    def __init__(self, character):
        self.char = character
        self.children = {}

    '''
    used for when we are determining if a string exists in our trie
    '''
    def __eq__(self, other):
        return self.char == other

    '''
    used for testing set membership
    '''
    def __hash__(self):
        return hash(self.char)


trie = Trie()
trie.add_word("this")
trie.add_word("that")
print(trie.has_word("this"))
print(trie.has_word("thisa"))
print(trie.has_prefix("th"))
print(trie.has_prefix("ta"))
trie.add_word("thataaaa")

