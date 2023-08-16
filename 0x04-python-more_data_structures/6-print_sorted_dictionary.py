#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    my_keys = sorted(a_dictionary.keys())
    for key in my_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
