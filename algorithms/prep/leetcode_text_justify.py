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
        cur_len = 0
        while i < n:
            if cur_len + len(words[i]) + len(cur_words) < maxWidth:
                cur_words.append(words[i])
                cur_len += len(words[i])
            else:
                added_space = [x + " " for x in cur_words]
                justified = self.justify_line(added_space, maxWidth-cur_len)
                res.append(justified)
                cur_words = [words[i]]
                cur_len = len(words[i]) + 1

            i += 1
        # now we're on the last line
        if cur_words:
            last = self.justify_last(cur_words, remains)
            res.append(last)

        return res

    def justify_line(self, line_array, spaces):
        # what if the last word in the line_array ends with a space?
        if len(line_array) == 1:
            return line_array[0] + (" "*spaces)

        result = []

        # calculate remaining spaces to distribute
        slots = len(line_array) - 1
        per_slot = spaces // slots
        remaining = spaces % slots

        for i in range(len(result) - 1):
            result[i] = result[i] + (" " * per_slot)

        for i in range(len(result) - 1):
            if remaining > 0:
                result[i] = result[i] + " "
            remaining-=1

        return "".join(result)

    def justify_last(self, line, spaces):
        # if this is the last line, left justify it and return
        return "".join(line) + (" " * spaces)

sol = Solution()

data=["What","must","be","acknowledgment","shall","be"]

size = 16

output = sol.fullJustify(data, 16)

print(output)


'''
what information do we need to justify a line of text?
if there is only one word, it is left justified
if there are two or more words, we fully justify it
'''
def justify_line(line_array, spaces):
    #what if the last word in the line_array ends with a space?
    if len(line_array) == 1:
        return "".join([line_array[0] + (" " * spaces)])
    result = []
    for i in range(len(line_array)-1):
        result.append(line_array[i] + " ")
        spaces-=1
    result.append(line_array[-1])
    #calculate remaining spaces to distribute
    slots = len(line_array) - 1
    per_slot = spaces // slots
    remaining = spaces % slots

    for i in range(len(result)-1):
        result[i] = result[i] + (" "*per_slot)

    for i in range(len(result)-1):
        if remaining>0:
            result[i] = result[i] + " "

    return result