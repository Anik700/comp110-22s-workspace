"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730243145"


class Simpy:
    """Creating a Simpy Object."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializing values."""
        self.values = values

    def __str__(self) -> str:
        """Produce a String Representation of Simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, num: int) -> None:
        """Mutate Values with a specific number of repeating values."""
        if(len(self.values) > 0):
            last_val = self.values[-1]
        else:
            last_val = value
        if(last_val == value):
            size_diff = num - len(self.values)
            if size_diff >= 0:
                while size_diff > 0:
                    self.values.append(value)
                    size_diff -= 1
            else:
                self.values = self.values[0: len(self.values) + size_diff]
        else:
            self.values = list()
            while num > 0:
                self.values.append(value)
                num -= 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Filling in Values with range of values."""
        assert step != 0.0

        if start <= stop:
            assert step > 0
            while start < stop:
                self.values.append(start)
                start += step
        else:
            assert step < 0
            while start > stop:
                self.values.append(start)
                start += step
        return None

    def sum(self) -> float:
        """Compute the sum of all items in values attribute."""
        Sum = sum(self.values)
        return Sum

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overloading the '+' Operator."""
        if type(self) == type(rhs):
            result = []
            if len(self.values) == len(rhs.values):
                i = 0
                while i < len(self.values):
                    result.append(self.values[i] + rhs.values[i])
                    i += 1
        else:
            n = 0
            result = []
            while n < len(self.values):
                result.append(self.values[n] + rhs) 
                n += 1

        return Simpy(result)

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overloading the '**' Operator."""
        if type(self) == type(rhs):
            result = []
            if len(self.values) == len(rhs.values):
                i = 0
                while i < len(self.values):
                    result.append(self.values[i] ** rhs.values[i])
                    i += 1
        else:
            n = 0
            result = []
            while n < len(self.values):
                result.append(self.values[n] ** rhs) 
                n += 1

        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Creating a Mask based on equality of values and Simpy/float value."""
        if type(self) == type(rhs):
            result = []
            if len(self.values) == len(rhs.values):
                i = 0
                while i < len(self.values):
                    result.append(self.values[i] == rhs.values[i])
                    i += 1
        else:
            n = 0
            result = []
            while n < len(self.values):
                result.append(self.values[n] == rhs) 
                n += 1

        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Create a mask basked on the greater than relationship."""
        if type(self) == type(rhs):
            result = []
            if len(self.values) == len(rhs.values):
                i = 0
                while i < len(self.values):
                    result.append(self.values[i] > rhs.values[i])
                    i += 1
        else:
            n = 0
            result = []
            while n < len(self.values):
                result.append(self.values[n] > rhs) 
                n += 1

        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adding the ability to use the subscription operator."""
        if(type(rhs) == int):
            result = []
            for item in self.values:
                if(item > rhs):
                    result.append(item)
        else:
            result = []
            i = 0
            while i < len(rhs):
                if rhs[i] is True:
                    result.append(self.values[i])
                i += 1
        return Simpy(result)