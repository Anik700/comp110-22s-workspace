"""Utilities Funcitons Test. """

__author__ = "73024145"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_1() -> None:
    input_list: list[int] = [111,12,13,14,15,16]
    assert only_evens(input_list) == [12,14,16]

def test_only_evens_2() -> None:
    input_list: list[int] = [23423,54654,67567,4535,15,16, 2342]
    assert only_evens(input_list) == [54654,16,2342]

#Edge case
def test_only_evens_3() -> None:
    input_list: list[int] = []
    assert only_evens(input_list) == []

def test_sub_1() -> None:
    input_list: list[int] = [1,2,3,4,5]
    assert sub(input_list,1,3) == [2,3,4]

def test_sub_2() -> None:
    input_list: list[int] = [23,34,8,6,24,32]
    assert sub(input_list,1,3) == [34,8,6]

#Edge case
def test_sub_3() -> None:
    input_list: list[int] = []
    assert sub(input_list,1,3) == []


def test_concat_1() -> None:
    input_list1: list[int] = [4,3,1,5,6]
    input_list2: list[int] = [23,45,65,76,87]
    assert concat(input_list1,input_list2) == [4,3,1,5,6,23,45,65,76,87]

def test_concat_2() -> None:
    input_list1: list[int] = [1,2,3]
    input_list2: list[int] = [4,5]
    assert concat(input_list1,input_list2) == [1,2,3,4,5]

#edge case
def test_concat_3() -> None:
    input_list1: list[int] = [4,3,1,5,6]
    input_list2: list[int] = []
    assert concat(input_list1,input_list2) == [4,3,1,5,6]
