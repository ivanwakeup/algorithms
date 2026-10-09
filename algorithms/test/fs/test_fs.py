'''
tests for algorithms/fs/fs.py

run from the repo root:
    pytest algorithms/test/fs -v
    pytest algorithms/test/fs -k mkdir      # only tests with "mkdir" in the name

paths are absolute and "/"-separated, e.g. "/a/b/c" (like LeetCode 588)
'''
import pytest

from algorithms.fs.fs import FileSystem


@pytest.fixture
def fs():
    return FileSystem()   # every test that takes `fs` gets a fresh, empty one


# --- mkdir ---

def test_mkdir_single(fs):
    fs.mkdir("a")

    assert "a" in fs.root.children

def test_mkdir_nested(fs):
    fs.mkdir("a/b/c")
    assert fs.ls("/a") == ["b"]
    assert fs.ls("/a/b") == ["c"]


def test_mkdir_special_chars_rejected(fs):
    with pytest.raises(ValueError):
        fs.mkdir("/a$b")


def test_add_content_to_file(fs):
    fs.mkdir("a")
    fs.add_content_to_file("/a/test.txt", "hello!")
    assert "".join(fs.root.children["a"].children["test.txt"].content) == "hello!"

    fs.add_content_to_file("/a/test.txt", " hello again!")
    assert "".join(fs.root.children["a"].children["test.txt"].content) == "hello! hello again!"


# --- ls ---

def test_ls_empty_root(fs):
    assert fs.ls("/") == []

# TODO: results sorted, ls on a file returns [filename], ls on a missing path


# --- add_content_to_file ---

# TODO: create a file, append to an existing file, file in a nested dir
