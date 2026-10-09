'''
python in-memory fs with (ls, mkdir, addContentToFile)
'''

class InvalidPathError(ValueError):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class FSNode:

    def __init__(self, name, dir=False) -> None:
        self.name = name
        self.children = {}
        self.is_directory = dir
        self.content = []


class FileSystem:

    def __init__(self):
        self.root = FSNode("root", dir=True)
        self.current_dir = self.root

    def ls(self, dir):
        parsed_dirs = self._get_path_list(dir)
        cur = self.root
        for dir in parsed_dirs:
            if dir not in cur.children:
                raise InvalidPathError(f"path at {dir} does not exist!")
            if not cur.children[dir].is_directory:
                return dir
            cur = cur.children[dir]
        if cur.is_directory:
            return list(cur.children.keys())
        else:
            return cur.name


    def add_content_to_file(self, filepath, data):
        path = self._get_path_list(filepath)
        if not path:
            raise InvalidPathError("no filepath supplied!")
        cur = self.root
        for i, part in enumerate(path):
            if i == len(path)-1:
                if part in cur.children:
                    node = cur.children[part]
                    if node.is_directory:
                        raise InvalidPathError(f"{part} is a directory!")
                else:
                    node = FSNode(part, dir=False)
                    cur.children[part] = node
                node.content.append(data)
            else:
                if part not in cur.children:
                    raise InvalidPathError("path doesn't exist!")
                cur = cur.children[part]
                if not cur.is_directory:
                    raise InvalidPathError("file encountered in path")
                

    def mkdir(self, dir_path):
        paths = self._get_path_list(dir_path)
        cur = self.root
        for item in paths:
            if item not in cur.children:
                dir = FSNode(item, dir=True)
                cur.children[item] = dir
            cur = cur.children[item]
            if not cur.is_directory:
                raise InvalidPathError(f"{cur.name} is a file!")


    def _get_path_list(self, dir_str):
        special_chars = ["$", "\\"]
        if any(c in dir_str for c in special_chars):
            raise ValueError(f"cannot construct dir with special chars {special_chars}")
        return list(filter(lambda x: x != '', dir_str.split("/")))

         
                

        

