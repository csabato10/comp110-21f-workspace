"""List utility functions part 2."""

__author__ = "730466575"

# Define your functions below

"""Only evens."""


def only_evens(numbs: list[int]) -> list[int]:
    """Returns only even numbers of a list."""
    evens: list[int] = []
    for numb in numbs:
        if numb % 2 == 0:
            evens.append(numb) 
    return evens


"""Sub."""


def sub(b: list[int], start: int, end: int) -> list[int]:
    """Returns list values at given indices."""
    indexed_list: list[int] = []
    if len(b) == 0 or start >= len(b) or end <= 0:
        return indexed_list
    
    if start < 0:
        indexed_list.append(b[0])
    else:
        indexed_list.append(b[start])
    
    if end > len(b):
        indexed_list.append(b[-1])
    else:
        indexed_list.append(b[end])
    return indexed_list


"""Concat."""


def concat(a: list[int], b: list[int]) -> list[int]:
    """Combines two lists into one."""
    new_list: list[int] = []
    for value in a:
        new_list.append(value)
    for value in b:
        new_list.append(value)
    return new_list
    
