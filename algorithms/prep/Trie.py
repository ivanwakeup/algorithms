'''
A trie contains an empty root, and each child node is the next letter in some word that you add
searching in a try takes 0(h) time, where h is the height of the tree
the height of the tree is at most len(longest_word) in the Trie
'''

class Trie:

    def __init__(self):
        self.trie = {}

    def add_word(self, word):
        search = self.trie
        while word[0] in search:
            search = search[word[0]]
            word = word[1:]
        while word:
            next = word[1] if len(word) > 1 else "*"
            search[word[0]] = {next: {}}
            search = search[word[0]]
            word = word[1:]

    def has_prefix(self, prefix):
        if not prefix:
            return False
        search = self.trie
        while prefix:
            if prefix[0] in search:
                search = search[prefix[0]]
                prefix = prefix[1:]
            else:
                return False
        return prefix == ''

    def has_word(self, word):
        if not word:
            return True
        search = self.trie
        while word:
            if word[0] in search:
                search = search[word[0]]
                word = word[1:]
            else:
                return False
        return not word and "*" in search


t = Trie()

t.add_word("this")
t.add_word("that")
t.add_word("what")
t.add_word("thatisit")
print(t.trie)


print(t.has_prefix("wh"))

print(t.has_word("thatisnot"))