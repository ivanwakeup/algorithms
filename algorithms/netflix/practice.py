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


'''
  Movie Billboard Service

  A streaming service has a billboard that shows one featured title at a time. Titles have scores, which can change at any time. Implement:

  - upsert_title(title_id: str, score: float) -> None
    - Add a title with the given score, or update the score if the title already exists.
    - It can be called at any time, including for the title currently on the billboard.
  - get_top_title() -> MovieState | None
    - Rotate the billboard: show the highest-scoring title that is not currently shown, and return it.
    - The title it replaces becomes eligible again for later calls, using its latest score.
    - Return None if no title is eligible.
    - (Assumption) If only one title exists, the second call returns None. Decide whether the billboard should keep showing that title instead.


SOLUTION:
data structures + invariants
hm: the current state for a given movie, its current score
pq: candidate movies, with the next highest scoring candidate at the top
current_movie_variable: the currently shown movie on the billboard.

basically dont add a movie to the heap if its currently being shown. just update its state

implementation details:
1. get_top_title returns None if nothing is eligible, or it returns the current_movie_variable, which is updated during get_top_title.
2. only add a movie to the pq if it ISNT the current movie.
3. stale entries defined by version number--which is updated in the HM when a title comes in. 
if the version in the heap doesn't match the current state, it isnt a candidate. discard it.

so in the heap, its possible that current movie = A and there are stale A entries in the heap. so there are two possibilities:
    1. heap top is the same movie as currently shown=> it MUST be stale given that we only add a movie to heap if its not the same as cur
    2. heap top is a different movie=>might still be stale, check version
'''

from dataclasses import dataclass

@dataclass
class MovieState:
    title_id: str
    score: float
    version: int

from queue import PriorityQueue
class MovieBillboardService:

    def __init__(self) -> None:
        self.pq = PriorityQueue()
        self.hm = {}
        self.current_movie = None
        
    #add candidates to PQ, but not if its the current movie. we will add current movie back on to queue once something replaces it
    def upsert_title(self, title_id, score):
        version = self.hm[title_id].version+1 if title_id in self.hm else 1
        item = MovieState(title_id, score, version)
        self.hm[title_id] = item
        if self.current_movie and self.current_movie.title_id == title_id:
            #make sure current_movie is always the latest version, otherwise when we add it back to the heap (when a new movie is shown) we might accidently push the expired version
            self.current_movie = item
            return
        self.pq.put((-item.score, item.title_id, item.version))

    def get_top_title(self):
        while not self.pq.empty():
            _, title, version = self.pq.get()
            if version != self.hm[title].version:
                continue
            #now its impossible that current_movie == the heap item, thanks to our upsert_title. so this must be a valid entry
            if self.current_movie:
                put_back = self.current_movie
                self.pq.put((-put_back.score, put_back.title_id, put_back.version))
            self.current_movie = self.hm[title]
            return self.current_movie
        return None
            


        


def recipe_checker(recipes, required):
    r_set = set(required)
    result = []
    for recipe in recipes:
        to_add = []
        matches = set()
        for ingredient in recipe:
            if ingredient in r_set:
                matches.add(ingredient)
            else:
                to_add.append(ingredient)
        if matches == r_set:
            result.extend(to_add)
    return set(result)
                


                



        
    
    
    
