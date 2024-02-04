#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        value_as_integer = int(value)  # Intenta convertir el valor en un entero
        print(value_as_integer)  # Imprime el valor entero
        return True
    except ValueError:
        sys.stderr.write("Exception: {} is not an integer\n".format(value))  # Maneja el error
        return False
