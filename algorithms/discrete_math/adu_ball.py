'''
write a program to find combinations of 7 and 11 that will give you any input N greater than 60


could do this in a "backtracking" style, where we try combinations and keep going until we hit our target number.
'''

def find_combo(n, cur_sum, path):
    if cur_sum > n:
        return False
    if cur_sum == n:
        print(path)
        return True
    with_sev = find_combo(n, cur_sum+7, path+[7])
    with_elev = find_combo(n, cur_sum+11, path+[11])
    return max(with_elev, with_sev)

find_combo(65, 0, [])
