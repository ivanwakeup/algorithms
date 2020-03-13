'''
input:
N, number of words to hydrate trie with
N-lines of words
K, prefixes to check
K-lines of prefixes

read stdin, return list of possible words for the autocomplete?
'''


class Trie:

    def __init__(self):
        self.root = {}

    def add_word(self, word):
        t = self.root
        for char in word:
            if char in t:
                t = t[char]
            else:
                t[char] = {}
                t = t[char]
        t["#"] = "#"

    def traverse(self, prefix):
        t = self.root
        for char in prefix:
            if char not in t:
                return None
            t = t[char]
        return t

    def has_prefix(self, prefix):
        if self.traverse(prefix):
            return True
        return False

    def has_word(self, word):
        t = self.root
        if self.traverse(word):
            return "#" in t
        return False

    def get_words_for_prefix(self, prefix):
        t = self.traverse(prefix)
        if not t:
            return []
        result = []

        def do_get(node, curr):
            if "#" in node:
                result.append(curr)
            for key in node.keys():
                if key == "#":
                    continue
                do_get(node[key], curr+key)
            return

        do_get(t, prefix)
        return result


def get_words_and_prefixes(file_obj):
    num_words = int(file_obj.readline().strip())
    words = []
    cur = 0
    while cur < num_words:
        words.append(file_obj.readline().strip())
        cur+=1
    num_prefixes = int(file_obj.readline().strip())
    prefixes = []
    cur = 0
    while cur < num_prefixes:
        prefixes.append(file_obj.readline().strip())
        cur+=1
    return words, prefixes


def generate_output(words, prefixes):
    t = Trie()
    output = []
    for word in words:
        t.add_word(word)
    for prefix in prefixes:
        output.append(t.get_words_for_prefix(prefix))
    return output


with open('autocompleter.txt') as f:
    words, prefixes = get_words_and_prefixes(f)
    output = generate_output(words, prefixes)
    print(output)








