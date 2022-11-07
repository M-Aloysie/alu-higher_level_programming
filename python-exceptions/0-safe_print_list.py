#!/usr/bin/python3
# A  function that prints x elements of a list


def safe_print_list(my_list=[], x=0):
    ret = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)

