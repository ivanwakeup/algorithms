'''
we have some input text, let's justify it (as if in an editor) so the lines look the best

define some quantity BADNESS(line) that tells us how bad a line is

we want to then wind up with the minimum badness for all of the input lines!
'''

def get_min_cost(words, memo):
    key = ":".join(words)
    if key in memo:
        return memo[key]
    if not words:
        return 0
    min_cost = float('inf')
    for i in range(len(words)):
        local_bad = badness(words[:i+1])
        cost = get_min_cost(words[i+1:], memo)
        min_cost = min(min_cost, local_bad+cost)
    memo[key] = min_cost
    return min_cost

'''
get the badness cost of this line
'''
def badness(line_arr, total_width=15):
    line_len = sum([len(x) for x in line_arr])
    if line_len > total_width:
        return float('inf')
    return (total_width - line_len)**3


data = ["aa", "bb", "ccdc", "wowhfnal", "dkaa", "eekfja",
        "asadha", "as", "ash", "asyay4", "hadhadh", "ahda", "ashdasdh", "asdhasdh", "aet.", "asdhasjhdasj"]
print(get_min_cost(data, {}))


'''
problems, what if we have a word that is longer than fits on a single line?

'''