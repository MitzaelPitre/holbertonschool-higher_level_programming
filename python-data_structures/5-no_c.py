#!/usr/bin/python3

def no_c(mystring):
    new_str = ''
    for i in mystring:
        if i != 'C' and i != 'c':
            new_str += i

    return new_str
