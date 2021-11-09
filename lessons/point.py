"""Example of a Point class."""

from __future__ import annotations

 
class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        """Initialize a Point with its x, y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies componenets by factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Pure method that does not mutate the Point."""
        return Point(self.x * factor, self.y * factor)

    def __str__(self) -> str:
        """Produce a str representation of a Point for humans"""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Priduce a str representation of a Point for Python!"""
        return f"Poinnt({self.x}, {self.y})"


p0: Point = Point(1.0, 2.0)
p0.scale_by(2.0)
print(p0)
print(f"{p0.x}, {p0.y}")

p1: Point = p0.scale(2.0)
print(f"{p1.x}. {p1.y}")

p1_as_a_str: str = str(p1)
print(p1_as_a_str)

p1_repr: str = repr(p1)
print(p1_repr)
