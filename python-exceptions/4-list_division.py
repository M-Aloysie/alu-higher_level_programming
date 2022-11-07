#!/usr/bin/python3
# A function that divides element by element two lists


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for k in range(0, list_length):
        try:
             div = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
