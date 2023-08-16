#!/usr/bin/python3

def number_keys(a_dictionary):
    sum = 0
    for i, keys in enumerate(a_dictionary, start=1):
        sum += i
    return i
