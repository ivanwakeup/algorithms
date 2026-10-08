'''
python in-memory fs with (ls, mkdir, addContentToFile)
'''


class DirectoryNode:

    def __init__(self, name) -> None:
        self.name = name
        self.parent = None
        self.children = None

class File:

    def __init__(self, name) -> None:
        self.name = name
        self.buffer = []

    def add_bytes(self, bytes):


        
class FileSystem:

    def __init__(self):
        pass

    def ls():
        pass

    d