'''
tests for recipe_checker in algorithms/netflix/practice.py

recipe_checker(recipes, required) returns the set of extra ingredients (not in
`required`) from every recipe that contains ALL of the required ingredients.

run from the repo root:
    pytest algorithms/test/netflix/test_recipe_checker.py -v
'''
from algorithms.netflix.practice import recipe_checker


# --- basic matching ---

def test_single_matching_recipe():
    recipes = [["egg", "milk", "flour"]]
    assert recipe_checker(recipes, ["egg", "milk"]) == {"flour"}


def test_only_recipes_with_every_required_ingredient_count():
    recipes = [
        ["egg", "milk", "flour"],   # has both -> counts
        ["egg", "sugar"],           # missing milk -> ignored
        ["milk", "butter"],         # missing egg -> ignored
    ]
    assert recipe_checker(recipes, ["egg", "milk"]) == {"flour"}


def test_extras_combined_across_matching_recipes():
    recipes = [
        ["egg", "milk", "flour"],
        ["milk", "egg", "sugar", "flour"],
    ]
    assert recipe_checker(recipes, ["egg", "milk"]) == {"flour", "sugar"}


def test_ingredient_order_does_not_matter():
    assert recipe_checker([["flour", "milk", "egg"]], ["egg", "milk"]) == {"flour"}


# --- nothing to return ---

def test_no_recipe_matches():
    recipes = [["egg", "flour"], ["milk", "sugar"]]
    assert recipe_checker(recipes, ["egg", "milk"]) == set()


def test_matching_recipe_with_no_extras():
    assert recipe_checker([["egg", "milk"]], ["egg", "milk"]) == set()


def test_no_recipes():
    assert recipe_checker([], ["egg"]) == set()


# --- duplicates ---

def test_duplicate_required_ingredients_are_ignored():
    assert recipe_checker([["egg", "milk", "flour"]], ["egg", "egg", "milk"]) == {"flour"}


def test_repeated_required_ingredient_does_not_stand_in_for_a_missing_one():
    # "egg" twice must not count as having both "egg" and "milk"
    recipes = [["egg", "egg", "flour"]]
    assert recipe_checker(recipes, ["egg", "milk"]) == set()


# --- edge cases ---

def test_no_required_ingredients_matches_every_recipe():
    recipes = [["egg", "flour"], ["milk"]]
    assert recipe_checker(recipes, []) == {"egg", "flour", "milk"}
