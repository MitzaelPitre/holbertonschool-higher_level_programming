#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        value_as_integer = int(value)
        print(value_as_integer)
        return True
    except ValueError:
        sys.stderr.write("Exception: {} is not an integer\n".format(value))
        return False
