#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    tuple_b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b[:2]

    sum1 = tuple_a[0] + tuple_b[0]
    sum2 = tuple_a[1] + tuple_b[1]

    return (sum1, sum2)

if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))

    print(add_tuple((1,), (2, 3)))  # (3, 3)
    print(add_tuple((1, 2, 3), (4, 5, 6))) 
