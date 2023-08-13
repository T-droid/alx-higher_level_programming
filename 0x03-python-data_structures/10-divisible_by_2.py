#!/bin/python3

def divisible_by_2(my_list=[]):
    bool_table = []
    for idx, i in enumerate(my_list):
        if i % 2 == 0:
            bool_table.append(True)
        else:
            bool_table.append(False)

    return bool_table
