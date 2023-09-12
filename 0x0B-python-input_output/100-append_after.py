#!/usr/bin/python3

"""module to define inserting function"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of textto a file
    Args:
        filename(str): name of the file
        search_strings(str): string to be searched
        new_string(str): new string to be inserted
    """
    res_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            res_line += [line]
            if line.find(search_string) != -1:
                res_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(res_line))
