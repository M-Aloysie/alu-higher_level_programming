#!/usr/bin/python3
# A function that first prints the first x elements
# Of a list and integers only


def safe_print_list_integers(my_list=[], y=0):
    ret = 0
    for j in range(0, y):
        try:
            print("{:d}".format(my_list[j]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
