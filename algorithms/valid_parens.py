# every opening paren should have a matching closing paren
# keep track
# every close must be preceeded by an open

def valid_parens(s):
    if len(s) % 2 != 0:
        return False
    if not s:
        return False
    valid_map = {")": "(", "}": "{", "]": "["}
    if s[0] in valid_map.keys():
        return False
    stack = []
    for char in s:
        if char not in valid_map.keys():
            stack.append(char)
        else:
            if valid_map[char] != stack.pop():
                return False
    return len(stack) == 0


if __name__ == "__main__":
    test_cases = [
        ("{}{}", True),
        ("{}", True),
        ("({)}", False),
        ("{[]}", True),

    ]
    for input, output in test_cases:
        assert(valid_parens(input) == output)