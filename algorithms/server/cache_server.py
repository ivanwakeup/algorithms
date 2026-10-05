import socket
from algorithms.caching.caching import TTLCache
import sys


def handle_commands(cmd, cache):
    cmd_arr = cmd.strip().split()
    if cmd_arr[0] not in ["GET", "SET"]:
        return """Invalid operation, please use one of: ["GET", "SET"]"""
    if cmd_arr[0] == "GET":
        return str(cache.get(cmd_arr[1]))
    if cmd_arr[0] == "SET":
        cache.put(cmd_arr[1], cmd_arr[2])
        return f"SET value for {cmd_arr[1]} to {cmd_arr[2]}"
    return str(None)
    
    
def run_cache_server():
    HOST = "127.0.0.1"
    PORT = 64532  
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Server is listening on {HOST}:{PORT}...")
        cache = TTLCache(cache_size=3, ttl_seconds=10, eviction_thread=True)

        while True:
            # 4. Block and wait for a client connection
            # accept() returns a brand-new socket for data, and the client's address
            client_socket, client_address = server_socket.accept()
            
            with client_socket:
                print(f"Connected established with {client_address}")
                # 5. Receive and process data stream
                while True:
                    data = client_socket.recv(1024) # Read up to 1024 bytes
                    if not data:
                        break # Client disconnected
                    
                    result = handle_commands(data.decode('utf-8'), cache)
                    
                    # Echo the data back to the client
                    client_socket.sendall(b"\n" + result.encode('utf-8') + b"\n")
                
                print(f"Connection with {client_address} closed.")

if __name__ == "__main__":
    run_cache_server()