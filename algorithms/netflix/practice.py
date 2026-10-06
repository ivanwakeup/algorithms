'''
detect duplicates given a list of users

["bob", "alice", "rick", "alice"] -> "alice"
'''
from collections import Counter

def get_dupe_users(users):
    seen = set()
    result = set()
    for user in users:
        if user in seen:
            result.add(user)
        seen.add(user)
    return list(result)

def is_dupe_user(users, user):
    c = Counter(users)
    return c[user] > 1


data = [("alice", 30),
("bob",   11),
("alice", 12),
("alice", 31),
("alice", 10)]
'''
detect if a user appears more than once within a time window of size (window) seconds.
is the input sorted by time?
'''
from collections import defaultdict
def is_dupe_time_window(users, window=5):
    hm = defaultdict(list)
    sorted_hm = {}
    result = []
    for user, time in users:
        hm[user].append(time)

    for key, val in hm.items():
        sorted_hm[key] = list(sorted(val))

    for key, val in sorted_hm.items():
        for i in range(1, len(val)):
            if val[i]-val[i-1]<=window:
                result.append(key)
                break
    return result
    
    
    
