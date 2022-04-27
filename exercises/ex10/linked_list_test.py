"""Tests for linked list utils."""

from ast import Raise
import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730243145"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at1() -> None:
    """Testing Node when index is 0."""
    linked_list = Node(1, Node(2, Node(3, None)))
    index = 0
    assert value_at(linked_list, index) == 1


def test_value_at2() -> None:
    """Testing when a list is empty."""
    index = 1
    assert value_at(Node(1, Node(2, Node(3, None))), index) == 2


def test_max() -> None:
    """Testing max if its in the middle of a list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3


def test_max2() -> None:
    """Testing for multiple max values."""
    linked_list = Node(1, Node(2, Node(5, Node(5, None))))
    assert max(linked_list) == 5


def test_linkify() -> None:
    """Testing a normal list into a linked list. """
    input_list: list[int] = [1, 2, 3, 4]
    assert linkify(input_list).__str__() == Node(1, Node(2, Node(3, Node(4, None)))).__str__()


def test_linkify2() -> None:
    """Testing if input list is empty. """
    input_list: list[int] = []
    assert linkify(input_list) == None


def test_scale() -> None:
    """Testing whether input Node is scaled by int factor."""
    linked_list = Node(1, Node(2, Node(3, None)))
    factor: int = 2
    assert scale(linked_list, factor).__str__() == Node(2, Node(4, Node(6, None))).__str__()


def test_scale2() -> None:
    """Testing if head is equal to None."""
    linked_list = None
    factor: int = 2
    assert scale(linked_list, factor) == None