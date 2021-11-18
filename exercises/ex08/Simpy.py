"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730466575"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, nums: list[float]) -> None:
        """Initialize function."""
        self.values = nums

    def __str__(self) -> str:
        """Produce a str representaiton of a Point for humans!"""
        return f"Simpy{self.values}"

    def fill(self, value: float, n: int) -> None:
        """Fill in a class with the same value n times."""
        i: int = 0
        new_list: list[float] = []
        for i in range(n):
            new_list.append(value)
            i += 1
        
        self.values = new_list

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Add numbers to a class from one value to another given a certain step."""
        if step == 0.0:
            step = 1.0
  
        i: float = start

        new_list: list[float] = []
        while i != stop or i < stop:
            new_list.append(i)
            i += step
        
        self.values = new_list

    def sum(self) -> float:
        """Add up all the values in a class."""
        sum_total: float = 0.0
        for value in self.values:
            sum_total += value 
        return sum_total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add two classes or a class and one float."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        else:
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs)
                i += 1
        return result
            
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raise a class to the power of another class or just another power."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        else:
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs)
                i += 1
        return result

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Determine whether a class is equal to another class or float."""
        result: list[bool] = []
        i: int = 0
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        else:
            while i < len(self.values):
                result.append(self.values[i] == rhs)
                i += 1
        return result
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Determine whether a class is greater than another class or float."""
        result: list[bool] = []
        i: int = 0
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        else:
            while i < len(self.values):
                result.append(self.values[i] > rhs)
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Get to a value in a class."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            new_list: list[float] = []
                
            for i in range(len(rhs)):
                if rhs[i]:
                    new_list.append(self.values[i])

            self.values = (new_list)
            return self