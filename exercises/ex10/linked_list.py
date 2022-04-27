"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730243145"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next == None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the value at Index."""
    if index == 0:
        if head != None:
            return head.data
        raise IndexError("Index is out of bounds on the list.")
    else:
        if head == None:
            raise IndexError("Index is out of bounds on the list.")
        else:
            return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Returns the max value of linked list."""
    if head == None:
        return None
    else:
        if head.next == None:
            return head.data
        elif head.data > head.next.data:
            next = head.next
            head.next = next.next
            return max(head)
        else:
            return max(head.next)


def linkify(items: list[int]) -> Optional[Node]:
    """Converts list[int] to linked list."""
    if items == None or len(items) == 0:
        return None
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Scales a linked list by a factor."""
    if head == None:
        return None
    else:
        return Node(head.data * factor, scale(head.next, factor))
