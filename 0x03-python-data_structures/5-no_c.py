#!/bin/python3

def no_c(my_string):
    new = ""

    for i in my_string:
        if i != "C" and i != "c":
            new += i
    return new
