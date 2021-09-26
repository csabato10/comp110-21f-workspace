"""List utility functions."""

__author__ = "730466575"


# TODO: Implement your functions here.

def all(a: list[int], b: int) -> bool:
    """Determines whether an integer is present in a list."""
    i: int = 0
    while i < len(a):
        if a[i] == b:
            return True
        i += 1
    return False


def is_equal(list_one: list[int], list_two: list[int]):
    """Determines whether two lists are equal."""
    i: int = 0
    while i < len(list_one) or i < len(list_two):
        if list_one[i] == list_two[i]:
            i += 1
        else:
            return False
    return True


def max(list_example: list[int]):
    """Returns the maximum valued integer in a list."""
    if len(list_example) == 0:
        raise ValueError("max() arg is an empty List")
    max_value: int = 0
    i: int = 0
    while i < len(list_example):
        if max_value < list_example[i]:
            max_value = list_example[i]
        i += 1
    return max_value


given_list: list = [1, 2, 5, 7, 4]
print(max(given_list))