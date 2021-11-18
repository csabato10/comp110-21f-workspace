"""Examples of potional parameteres and Union type parameters."""

from typing import Union


def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting function."""
    # simple way to do this would've been f"Hello, {name}"
    result: str = "Hello, "
    if isinstance(name, str):
        return result + name
    elif isinstance(name, float):
        return result + "alien from sector " + str(name)
    else:
        return result + str(name)


# Calling hello with no agruments leads to use of default value
print(hello())
# Calling hello with one agrument overrides the default value
print(hello("Roch"))
print(hello(110))
print(hello(3.14))