#!/usr/bin/python3

"""module to create inheritence"""


class MyList(list):
    """class to inherit from list class"""

    def print_sorted(self):
        """method to print the list in sorted order"""
        newList = self[:]
        newList.sort()
        print(newList)
