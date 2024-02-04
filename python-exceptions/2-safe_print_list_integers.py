#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for item in my_list[:x]:  # Solo considera los primeros x elementos de la lista
        try:
            if isinstance(item, int):
                print("{:d}".format(item), end='')
                count += 1
        except TypeError:
            pass
    print()
    return count
