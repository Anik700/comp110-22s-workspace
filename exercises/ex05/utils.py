"""Utility Functions Exercise."""

__author__ = "730243145"

def only_evens(input_list: list[int]) -> list[int]:
   """Taking a list of int and returning only the even int values""" 


   #input_list: list[int] = list()
   even_num: list[int] = []

   for i in input_list:
       if i % 2 == 0:
           even_num.append(i)
   return even_num


def sub(input_list: list[int], start_ind: int, end_ind: int) -> list[int]:
    """Creating a Sublist from a list."""

    new_list: list[int] = []

    while start_ind <= end_ind:
        if len(input_list) == 0:
            return input_list
        if start_ind > len(input_list):
            return input_list
        if end_ind > len(input_list):
            return input_list
        else:
            new_list.append(input_list[start_ind])
            start_ind += 1
    return new_list 


def concat(first:list[int], second:list[int]) -> list[int]:
    """Concatenating two lists."""

    i = 0
    
    while i < len(second):
        first.append(second[i])
        i += 1
    return first
