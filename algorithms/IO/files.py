import sys
import os
import signal

def read_input_deregister_SIGINT():
    while True:
        signal.signal(signal.SIGINT, lambda x, y: print("haha got it!"))
        signal.signal(signal.SIGTERM, lambda x, y: print("haha got it!"))
        data = input()
        print(data)


def read_raw_file():
    f = open("data", "rb", buffering=0)
    f.seek(4)
    print(f.read(3))


read_raw_file()

