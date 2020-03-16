'''
we want to build a rate limiter that limits the number of requests a user can make per:
hour?
minute?
second?


1 -> 1
1 -> 2
1 -> 3
2 -> 1
2 -> 2


we need a data structure that helps us answer:
how many requests has user X made in the window CUR_REQUEST_TIMESTAMP - 1 HOUR?


options:
1. keep a hashmap of userid -> linked list of requests inserted by timestamp
    - when the first entry in the linked list falls outside of the window, we can remove it and move
      the list pointer forward until we're at the minimum of the window
2. store requests and timestamps in database, query for min request timestamp when request comes in



approach:
1. use the hashmap that stores requests as a cache for quick minimum lookup
2. also write requests and their timestamps to database
3. query database if cache miss


'''

