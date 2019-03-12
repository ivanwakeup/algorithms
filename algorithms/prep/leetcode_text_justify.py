'''
fix 1 - always remove the last space from the last word added in add_leftover_spaces

fix 2 - there are extra spaces
'''
class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        remains = maxWidth
        n = len(words)
        i = 0

        cur_words = []
        while i < n:
            if len(words[i]) + 1 <= remains:
                remains -= len(words[i]) + 1
                cur_words.append(words[i] + " ")
            else:
                # tHE LAST WORD OF A LINE WONT HAVE ANY SPACES AFTER IT, just before. so we need to modify the add_leftover_spaces routine
                justified = self.add_leftover_spaces(cur_words, remains)
                res.append(justified)
                remains = maxWidth - (len(words[i]) + 1)
                cur_words = [words[i] + " "]
            i += 1
        # now we're on the last line
        if cur_words:
            line = "".join(cur_words) + (" " * remains)
            res.append(line)

        return res

    def add_leftover_spaces(self, line_array, space_count):
        slots = max(1, len(line_array) - 1)
        to_add = space_count // slots
        remaining = space_count - (space_count - to_add)
        res = []
        for i in range(len(line_array) - 1):
            if remaining:
                res.append(line_array[i] + " " * (to_add + 1))
            else:
                res.append(line_array[i] + " " * to_add)
            remaining -= 1
        res.append(line_array[-1].strip())

        return "".join(res)


sol = Solution()

data = ["This", "is", "an", "example", "of", "text", "justification."]
size = 16

output = sol.fullJustify(data, 16)

print(output)