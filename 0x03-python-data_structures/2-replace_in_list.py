#!/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return None
    for i in my_list:
        if i == my_list[idx]:
            my_list[idx] = element
            break
    return my_list
