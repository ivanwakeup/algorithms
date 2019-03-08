'''
build trie
'''


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        rev = [word[::-1] for word in words]
        t = self.build_trie(rev)
        result = []
        for word in words:
            local_t = t
            for i in range(len(word)):
                char = word[i]
                if char in local_t:
                    local_t = local_t[char]
                else:
                    break
                    # now, just check if we can make a palindrome with the rest of the trie
            chk = self.can_form_palin(local_t, "")
            if chk:
                pass

    def build_trie(self, words):
        result = {}
        for word in words:
            trie = result
            for i in range(len(word)):
                char = word[i]
                if char in trie:
                    trie = trie[char]
                else:
                    trie[char] = {}
                    trie = trie[char]
                if i == len(word) - 1:
                    trie["*"] = {}
        return result

    '''
    i want to check if we can form a palindrome at the current starting point in the trie
    we could potentially have many branches, need to check each of them?
    any time we find a star, we've hit the end of a word so check if we made a palindrome

    but idk how to have the dynamic for loop at each trie level to check at each level if the key is present?

    maybe we can do it recursively
    '''

    def can_form_palin(self, trie_start, parent_str):
        if "*" in trie_start and parent_str[::-1] == parent_str:
            return True
        can_form = False
        for key in trie_start:
            nxt_trie = trie_start[key]
            can_form = max(can_form, self.can_form_palin(nxt_trie, parent_str + key))
        return can_form



sol = Solution()

trie = {u'a': {u'b': {u'c': {u'd': {'*': {}}}}}, u's': {u's': {u's': {u'l': {u'l': {'*': {}}}}}, '*': {}}, u'd': {u'c': {u'b': {u'a': {'*': {}}}}}, u'l': {u'l': {u's': {'*': {}}}}}
#trie = {'a': {"b": {"a" :{ "*": {}},"*": {}}}}

print(sol.can_form_palin(trie, ""))