'''
tests for MovieBillboardService in algorithms/netflix/practice.py

run from the repo root:
    pytest algorithms/test/netflix -v
    pytest algorithms/test/netflix -k upsert   # only tests with "upsert" in the name
'''
import pytest

from algorithms.netflix.practice import MovieBillboardService


@pytest.fixture
def svc():
    return MovieBillboardService()   # every test that takes `svc` gets a fresh, empty one


# --- get_top_title ---

def test_get_top_title_empty(svc):
    assert svc.get_top_title() is None


def test_get_top_title_single(svc):
    svc.upsert_title("a", 5.0)
    assert svc.get_top_title().title_id == "a"


def test_get_top_title_highest_score_wins(svc):
    svc.upsert_title("a", 1.0)
    svc.upsert_title("b", 9.0)
    svc.upsert_title("c", 5.0)
    assert svc.get_top_title().title_id == "b"

# TODO: calling twice in a row (should the same title repeat? what if it's the only one?)
# TODO: ties on score (which title wins, and is that intended?)


# --- upsert_title ---

def test_upsert_lowered_score_drops_title(svc):
    svc.upsert_title("a", 5.0)
    svc.upsert_title("b", 3.0)
    svc.upsert_title("a", 1.0)   # old (a, 5.0) entry is now stale
    assert svc.get_top_title().title_id == "b"


def test_two_titles_dupe_returns_none(svc):
    svc.upsert_title("a", 2.0)
    svc.upsert_title("a", 3.5)
    assert svc.get_top_title().title_id == "a"
    assert svc.get_top_title() == None



# TODO: raised score moves a title to the top
# TODO: version increments on each upsert


def test_upsert_current_title_not_lost(svc):
    svc.upsert_title("a", 5.0)
    svc.upsert_title("b", 3.0)
    assert svc.get_top_title().title_id == "a"

    svc.upsert_title("a", 10.0)   # bump the title that's on the billboard right now
    assert svc.get_top_title().title_id == "b"

    top = svc.get_top_title()     # a must come back, with its new score
    assert top is not None
    assert (top.title_id, top.score) == ("a", 10.0)
