"""List utility functions."""

__author__ = "730466575"


# TODO: Implement your functions here.

def all(a: list[int], b: int) -> bool:
    """Determines whether an integer is present in a list."""
    i: int = 0
    while i < len(a):
        if a[i] != b:
            return False
        i += 1
    return True


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Determines whether two lists are equal."""
    i: int = 0
    if len(list_one) == len(list_two):
        while i < len(list_one):
            if list_one[i] == list_two[i]:
                i += 1
            else:
                return False
    else:
        return False
    return True


def max(list_example: list[int]) -> int:
    """Returns the maximum valued integer in a list."""
    if len(list_example) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max_value: int = list_example[i]
    while i < len(list_example):
        if max_value <= list_example[i]:
            max_value = list_example[i]
        i += 1
    return max_value
