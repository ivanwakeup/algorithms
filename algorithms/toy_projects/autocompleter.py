'''
input:
N, number of words to hydrate trie with
M, number of words to check in trie
N-Lines of words
M-Lines of words to check

read stdin, return list of possible words for the autocomplete?
'''

import fileinput


class Trie:

    def __init__(self):
        self.root = [{}, []]

    def add_word(self, word, rank):
        t = self.root[0]
        for char in word:
            if char in t:
                t[1].append([word, rank])
                t = t[0]
            else:
                t[char] = [{}, [[word, rank]]]
                t = t[char]
        t["#"] = "#"

    def traverse(self, prefix):
        t = self.root
        for char in prefix:
            if char not in t:
                return None
            t = t[char]
        return t

    def get_words_at_prefix(self, prefix):
        t = self.traverse(prefix)
        return t[1]

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
    num_prefixes = int(file_obj.readline().strip())
    words = []
    prefixes = []
    for line in range(num_words):
        words.append([file_obj.readline().strip(), line])
    for line in range(num_prefixes):
        prefixes.append(file_obj.readline().strip())
    return words, prefixes


def generate_output(words, prefixes):
    t = Trie()
    output = []
    for word in words:
        t.add_word(word)
    for prefix in prefixes:
        output.append(t.get_words_for_prefix(prefix))
    return output


with fileinput.input() as f:
    words, prefixes = get_words_and_prefixes(f)

with open('autocompleter.txt') as f:
    words, prefixes = get_words_and_prefixes(f)
    output = generate_output(words, prefixes)
    print(output)








