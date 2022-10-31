#!/usr/bin/python3

def element_at(my_list, idx):
    for j in my_list:
        print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
