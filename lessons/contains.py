"""Example of a function that produces a list."""

# Define a function named contains
# We can give two values: a needle value being searched for in a haystack list


def contains(needle: str, haystack: list[str]) -> bool:
    # Return True if needle is found in haystack
    # Loop through each index in loop
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            # Test if item stored equals needle
            # Return true if so
            return True
        i += 1
    # Return false after testing each item
    return False
