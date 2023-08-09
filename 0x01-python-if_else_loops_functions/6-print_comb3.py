#!/usr/bin/python3
for num in range(9):
    for k in range(num + 1, 10):
        if num * 10 + k < 89:
            print("{:d}{:d}".format(num, k), end=", ")
print("{:d}".format(89))
