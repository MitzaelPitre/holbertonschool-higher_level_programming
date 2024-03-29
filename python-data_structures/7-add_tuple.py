#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = validate_tuple(tuple_a)
    tuple_b = validate_tuple(tuple_b)

    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))

def validate_tuple(_tuple=()):
    if len(_tuple) < 2:
        if len(_tuple) == 1:
            _tuple = (_tuple[0], 0)
        elif len(_tuple) == 0:
            _tuple = (0, 0)
    elif len(_tuple) > 2:
        _tuple = (_tuple[0], _tuple[1])

    return _tuple

if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))

    print(add_tuple((1,), (2, 3)))
    print(add_tuple((1, 2, 3), (4, 5, 6)))
