'''
build an in-memory filesystem that supports 3 operations: mkdir, ls, and add_contents_to_file

design:
1. unix type filesystem, one root directory
2. works for tens of thousands of files, should use a hashmap for quick lookup of nodes in a path
3. errors if a given directory doesnt exist on mkdir, add_contents_to_file
4. cwd not important for now-> any of these 3 operations start from the root of the filesystem
5. permissions, timestamps, symlinks out of scope->these would require additional data on fs_nodes.
6. ls on a file name returns the filename, on a dir returns its contents

implementation details:
1. a class to represent an FSNode, which can be a dir or a file.
2. a walk method which walks as far as it can, given a list of path parts. errors for any invalid part are thrown here.
3. a path parser that returns the path to walk and the target

    examples:
        mkdir("/foo/bar/") -> if bar doesnt exist, we cant walk to it. so walk to foo and return a CUR pointer
        add_content_to_file("/foo/bar/test.txt") -> walk to bar, return its pointer, test.txt is created
        ls("/foo/") -> print all the children
        mkdir("////") -> parser returns no paths, nothing is walked
        mkdir("/a") -> walk to root (a.k.a. no steps taken), a is the target
'''

from dataclasses import dataclass

@dataclass
class FSNode:
    name: str
    children: dict
    content: list
    is_dir: bool

class InvalidPathError(ValueError):
    pass

class VirtualFS:

    def __init__(self) -> None:
        self.root = FSNode("root", {}, [], is_dir=True)

    def mkdir(self, path_str):
        paths, target = self._parse_path(path_str)
        if not target:
            raise InvalidPathError(f"no directory specified")
        cur = self._walk(paths)
        if target in cur.children:
            raise InvalidPathError(f"{target} already exists at location")
        new_node = FSNode(target, {}, [], is_dir=True)
        cur.children[target] = new_node

    def ls(self, path_str):
        paths, target = self._parse_path(path_str)
        cur = self._walk(paths)
        if not target:
            return list(cur.children.keys())
        if target not in cur.children:
            raise InvalidPathError(f"{target} does not exist in location!")
        if cur.children[target].is_dir:
            return list(cur.children[target].children.keys())
        else:
            return target

    def add_content_to_file(self, path_str, data):
        paths, target = self._parse_path(path_str)
        cur = self._walk(paths)
        if not target:
            raise InvalidPathError(f"no file specified!")
        if target in cur.children:
            if cur.children[target].is_dir:
                raise InvalidPathError(f"{target} is a directory!")
            else:
                cur.children[target].content.append(data)
                return
        new_node = FSNode(target, {}, [data], is_dir=False)
        cur.children[target] = new_node
            
    def _parse_path(self, path_str):
        if "$" in path_str:
            raise InvalidPathError("unsupported chars specified")
        paths = [x for x in path_str.split("/") if x != ""]
        return (paths[:-1], paths[-1] if paths else None)

    #all of the paths need to exist, otherwise error
    def _walk(self, paths):
        position = self.root
        for item in paths:
            if item not in position.children:
                raise InvalidPathError(f"{item} does not exist!")
            if not position.children[item].is_dir:
                raise InvalidPathError(f"{item} is a file!")
            position = position.children[item]
        return position
        

'''
VirtualFS + cd commands

1. we support .. and . for all operations. . means stay here, .. means go to parent
2. our methods need to handle logic for how far to walk. ls on a file should only walk UP TO the file
3. parse path can stay the same. but now the operations need to determine where to start our walk based on preceeding "/"
4. / means start from root, no preceeding slash means start from cwd

'''

from dataclasses import field
from typing import Any

@dataclass
class FSNodeWithParent:
    name: str
    children: dict
    content: list
    is_dir: bool
    #compare is false because it will cause an infinite recursion at the root, because root.parent = root
    parent: Any = field(default=None, repr=False, compare=False)


class VirtualFS2:

    def __init__(self) -> None:
        self.root = FSNodeWithParent("root", {}, [], is_dir=True, parent=None)
        #makes it so cd .. if we're already on the root works.
        self.root.parent = self.root
        self.cwd = self.root


    def mkdir(self, path_str):
        paths = self._parse_path(path_str)
        if not paths:
            raise InvalidPathError(f"no directory specified")

        start_node = self.root if path_str.startswith("/") else self.cwd
        target = paths[-1]
        cur = self._walk(paths[:-1], start_node)
        if target in cur.children:
            raise InvalidPathError(f"{target} already exists at location")
        if target == "." or target == "..":
            raise InvalidPathError(f"{target} name in reserved character: ., ..")
        new_node = FSNodeWithParent(target, {}, [], is_dir=True, parent=cur)
        cur.children[target] = new_node

    def ls(self, path_str):
        start_node = self.root if path_str.startswith("/") else self.cwd
        paths = self._parse_path(path_str)
        if not paths:
            return list(start_node.children.keys())

        cur = self._walk(paths[:-1], start_node)
        target = paths[-1]

        #in case we end with a relative path
        if target == "." or target == "..":
            cur = self._walk([target], cur)

        elif target not in cur.children:
            raise InvalidPathError(f"{target} does not exist in location!")
        
        elif cur.children[target].is_dir:
            cur = self._walk([target], cur)
        else:
            return target

        return list(cur.children.keys())


    def add_content_to_file(self, path_str, data):
        start_node = self.root if path_str.startswith("/") else self.cwd

        paths = self._parse_path(path_str)
        if not paths:
            raise InvalidPathError(f"no file specified")

        cur = self._walk(paths[:-1], start_node)
        target = paths[-1]

        if target == "." or target == "..":
            raise InvalidPathError("invalid target reserved character")
        
        if target in cur.children:
            if cur.children[target].is_dir:
                raise InvalidPathError(f"{target} is a directory!")
            else:
                cur.children[target].content.append(data)
                return
        new_node = FSNodeWithParent(target, {}, [data], is_dir=False, parent=cur)
        cur.children[target] = new_node


    def cd(self, path_str):
        if not path_str:
            self.cwd = self.root
            return self.cwd
        start_node = self.root if path_str.startswith("/") else self.cwd
        paths = self._parse_path(path_str)
        cur = self._walk(paths, start_node)
        self.cwd = cur
        return self.cwd



    def _parse_path(self, path_str):
        if "$" in path_str:
            raise InvalidPathError("unsupported chars specified")
        paths = [x for x in path_str.split("/") if x != ""]
        return paths

    def _walk(self, paths, start):
        cur = start
        for item in paths:
            if item == ".":
                continue
            if item == "..":
                cur = cur.parent
                continue
            elif item not in cur.children:
                raise InvalidPathError(f"{item} does not exist!")
            if not cur.children[item].is_dir:
                raise InvalidPathError(f"{item} is a file!")
            cur = cur.children[item]
        return cur
        


