import socket
from algorithms.caching.caching import TTLCache
import sys

def run_cache_server():
    HOST = "localhost"
    port = 64532  
    for line in sys.stdin:
        print(line)


if __name__ == "__main__":
    run_cache_server()