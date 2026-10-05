# Caching Cheat Sheet

> **The one thing to remember:** a cache is a **hashmap + an ordering structure**,
> with a **size limit**, and the ordering must **match your policy**.

---

## 1. Fundamentals

### A cache must have a size limit
A cache that can grow forever is a memory leak. Every `put` must *guarantee* the limit.
"Evict and hope something was removed" is not enough.

### Eviction policies: who goes when the cache is full?

| Policy   | Position means...   | Does `get` move the key?            | Typical structure                         |
|----------|---------------------|-------------------------------------|-------------------------------------------|
| **LRU**  | last time used      | ✅ yes, a read is a use              | `OrderedDict`, or hashmap + doubly linked list |
| **LFU**  | how often used      | ✅ yes, bumps the count              | hashmap + buckets per count + `min_freq`  |
| **FIFO** | insertion time      | ❌ no                                | `OrderedDict` / queue                     |
| **TTL**  | expiry time         | ❌ no (unless sliding, see below)    | `OrderedDict` (same TTL) or min-heap (per-key TTL) |

### The core pattern
- **Hashmap** → O(1) lookup by key
- **Ordering structure** → cheap answer to "who goes next?"

Most cache interview questions are this pattern in some form.

---

## 2. TTL Caches

### Lazy vs. active expiry: use both

| | **Lazy (passive)** | **Active (background sweep)** |
|---|---|---|
| When | on `get` | every N seconds |
| Guarantees | never return dead data | memory is reclaimed |
| Weakness | keys nobody reads stay in memory forever | needs a thread, so needs locking |

Redis uses both.

### Fixed vs. sliding expiration: a policy choice

| | **Fixed** | **Sliding** |
|---|---|---|
| Clock starts | at write | at every access |
| Use for | data that goes stale on a schedule (API responses) | idle timeouts (sessions) |
| Examples | Redis `EXPIRE`, Caffeine `expireAfterWrite` | Caffeine `expireAfterAccess` |

### The rule: whatever you do to expiry, you do to position
- Fixed → `get` does **not** move the key.
- Sliding → `get` refreshes `expires_at` **and** calls `move_to_end`.
- Changing one without the other breaks the ordering without raising any error.

### Expiry ordering makes the sweep cheap

**Same TTL for every key** → insertion order = expiry order → `OrderedDict`:
```python
# Sweep from the front until the first fresh key: O(number of expired keys)
while self.hm and self._is_expired(next(iter(self.hm.values()))):
    self.hm.popitem(last=False)
```
⚠️ Overwriting an existing key does **not** move it in a dict. Call `move_to_end(key)`.

**TTL per key** (e.g. `SET k v EX 30`) → insertion order ≠ expiry order → **min-heap**
of `(expires_at, key)`. When a key is overwritten, its old heap entry is now stale:
**skip stale entries when you pop them** (lazy deletion, like `SimpleCache.evict_lru`).

### Use a monotonic clock
`time.monotonic_ns()`, **not** `time.time()`. Wall-clock time can jump backwards
(NTP sync, daylight saving), which would make keys expire early or never.

---

## 3. Concurrency

### Check-then-act races
In Python, single operations are atomic, but **sequences are not**:
```
server:   key in self.hm        → True
sweeper:  popitem(...)          → removes key
server:   self.hm[key]          → KeyError 💥
```
Even `next(iter(d))` is two steps and can raise
`RuntimeError: OrderedDict mutated during iteration` without a lock.
**You won't find every race by reasoning, so lock everything.**

### Locking rules
1. **Lock the whole logical operation**, not individual lines.
2. **Reads need the lock too**, not just writes.
3. **Never wait while holding the lock.** Sleep, I/O and network calls happen outside it.
4. **Always use `with self._lock:`**, never bare `acquire()`/`release()`.

### Reentrancy: the deadlock trap
A plain `threading.Lock` deadlocks if the **same thread** acquires it twice:
```python
def put(self, ...):
    with self._lock:
        self.evict()        # evict also does `with self._lock:` → hangs forever
```
**Fix:** public methods take the lock, and `_private` helpers never do
(they assume the caller already holds it). `RLock` also works, but this rule is cleaner.

### Background thread lifecycle
- `daemon=True` → the thread is killed abruptly when the process exits (fine for in-memory data).
- Anything created and thrown away while the process keeps running (**tests!**) needs a `close()`:
```python
self._stop = threading.Event()

def _run(self):
    while not self._stop.wait(self._interval):   # can be interrupted, unlike sleep
        self.cleanup()

def close(self):
    self._stop.set()
    self._thread.join()
```

---

## 4. System Design Concepts

### Cache stampede (thundering herd)
A popular key expires → 1,000 requests miss at once → all hit the database.
- **Per-key lock / single-flight:** only one request refreshes the key, the rest wait.
- **TTL jitter:** add randomness to TTLs so keys don't expire together.

### Write strategies

| Strategy | How it works | Trade-off |
|---|---|---|
| **Cache-aside** | app reads DB on miss, fills cache | most common; first read is slow |
| **Write-through** | write cache + DB together | consistent; slower writes |
| **Write-back** | write cache, flush to DB later | fast; data loss if cache dies |

### Invalidation
- **TTL** = simplest invalidation: stale data lives for at most one TTL.
- When stale data isn't acceptable, **explicitly delete or update** cache keys
  whenever the source data changes. This is the hard part.

---

## 5. Where to see these in `caching.py`

| Class | Concepts |
|---|---|
| `SimpleCache` | LRU with a heap + lazy deletion of stale entries |
| `BetterLRUCache` | LRU with `OrderedDict` + `move_to_end` |
| `MyOrderedDict` | building `OrderedDict` yourself: hashmap + doubly linked list |
| `SimpleLFUCache` | LFU with count buckets + `min_freq` |
| `TTLCache` | lazy + active expiry, `OrderedDict` ordered by expiry, locking, background thread |
