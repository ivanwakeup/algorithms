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


from dataclasses import dataclass

@dataclass
class MovieState:
    title_id: str
    score: float
    version: int

from queue import PriorityQueue
class MovieBillboardService:

    def __init__(self) -> None:
        self.current_movie = None
        self.pq = PriorityQueue()
        self.hm = {}

    def upsert_title(self, title_id, score):
        #always just add the latest version to the map
        version = self.hm[title_id].version+1 if title_id in self.hm else 1
        movie = MovieState(title_id, score, version)
        self.hm[title_id] = movie

        if self.current_movie and title_id == self.current_movie.title_id:
            self.current_movie = movie
        else:
            self.pq.put((-movie.score, movie.title_id, movie.version))

    def get_top_title(self):
        #the current movie is never in the pq, so any valid entry is a different title
        while not self.pq.empty():
            score, title, version = self.pq.get()
            if version != self.hm[title].version:
                continue
            if self.current_movie:
                cur = self.current_movie
                self.pq.put((-cur.score, cur.title_id, cur.version))
            self.current_movie = self.hm[title]
            return self.current_movie
        return None



                



        
    
    
    
