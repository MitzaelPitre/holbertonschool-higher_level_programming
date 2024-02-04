def safe_print_list_integers(my_list=[], x=0):
    y = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                y += 1
        except IndexError:
            break
    print()
    return y
