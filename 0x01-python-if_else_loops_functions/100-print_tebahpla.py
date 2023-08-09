#!/usr/bin/python3
for j in range(122, 96, -1):
    if j % 2:
        j = j - 32
    print("{:c}".format(j), end="")
