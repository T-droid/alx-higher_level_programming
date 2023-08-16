#!/usr/bin/python3

def print_list_integer(my_list=[]):
    if not my_list:
        return
    for i in my_list[0:]:
        print("{:d}".format(i))
