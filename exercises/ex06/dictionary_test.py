"""Dictionary Tests."""
__author__ = "730243145"

import pytest
from dictionary import invert
from dictionary import favorite_color
from dictionary import count


# invert tests defined
def test_invert_1() -> None:
    """Invert Use Case Test 1."""
    input_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(input_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert2() -> None:
    """Invert Use Case Test 2."""
    input_dict: dict[str, str] = {'apple': 'cat'}
    assert invert(input_dict) == {'cat': 'apple'}


# Test suppposed to return a KeyError
def test_invert_3() -> None:
    """Invert Edge Case Test."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)      


# fav_color tests defined
def test_favorite_color_1() -> None:
    """Favorite Color Use Case Test 1."""
    input_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "Blue", "Kris": "Blue"}
    assert favorite_color(input_dict) == "Blue"


def test_favorite_color_2() -> None:
    """Favorite Color Use Case Test 2."""
    input_dict: dict[str, str] = {"Andrew": "yellow", "Aniketh": "blue", "John": "pink", "Logan": "pink"}
    assert favorite_color(input_dict) == "pink"


def test_favorite_color_3() -> None:
    """Favorite Color Edge Case Test."""
    input_dict: dict[str, str] = {"Marc": "yellow", "Chloe": "yellow", "Ezri": "Blue", "Kris": "Blue"}
    assert favorite_color(input_dict) == "yellow"


# count tests defined
def test_count_1() -> None:
    """Count Use Case Test 1."""
    input_list: list[str] = ['a', 'b', 'c', 'b']
    assert count(input_list) == {'a': 1, 'b': 2, 'c': 1}


def test_count_2() -> None:
    """Count Use Case Test 2."""
    input_list: list[str] = ['blue', 'red', 'red', 'yellow']
    assert count(input_list) == {'blue': 1, 'red': 2, 'yellow': 1}


def test_count_3() -> None:
    """Count Edge Case Test."""
    input_list: list[str] = ['red', 'red', 'red', 'yellow']
    assert count(input_list) == {'red': 3, 'yellow': 1}