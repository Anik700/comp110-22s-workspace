"""Utilities Funcitons Test. """

__author__ = "73024145"

from utils import only_evens
from utils import sub
from utils import concat

def test_sub_1() -> None:
    input_list: list[int] = [1,2,3,4,5]
    assert sub(input_list,1,3) == [2,3,4]

def test_sub_2() -> None:
    input_list: list[int] = [23,34,8,6,24,32]
    assert sub(input_list,1,3) == [34,8,6]

def test_sub_3() -> None:
    input_list: list[int] = [23,34,8,6,24,32]
    assert sub(input_list,1,3) == [34,8,6]