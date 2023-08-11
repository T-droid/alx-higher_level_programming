#!/usr/bin/python3

import sys

if __name__ == "__main__":
    length = len(sys.argv)
    print(length - 1, "arguments", end='')
    if length > 1:
        print(":")
        for i in range(1, length):
            print(i, ":", " ", sys.argv[i], sep='')
    else:
        print(".")
