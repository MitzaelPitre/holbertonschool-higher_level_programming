#!/usr/bin/python3
"""Text indentation function."""

def text_indentation(text):
    """Add indentation to text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in "?:.":
        text = (delimiter + "\n\n").join(
                [index.strip(" ") for index in text.split(delimiter)])

    print(text)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
