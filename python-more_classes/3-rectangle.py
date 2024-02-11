#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be non-negative")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be non-negative")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def draw(self):
        if self._width == 0 or self._height == 0:
            return "Rectangle with no area."

        rect_str = ""
        for _ in range(self._height):
            rect_str += '#' * self._width + '\n'
        return rect_str.rstrip('\n')

    def __str__(self):
        return f"Rectangle: width={self._width}, height={self._height}"

    def __repr__(self):
        return f"Rectangle(width={self._width}, height={self._height})"
