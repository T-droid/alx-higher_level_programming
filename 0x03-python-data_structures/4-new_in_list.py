#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy_list = my_list[:]
    for i in copy_list:
        if i == copy_list[idx]:
            copy_list[idx] = element
            break
    return copy_list
