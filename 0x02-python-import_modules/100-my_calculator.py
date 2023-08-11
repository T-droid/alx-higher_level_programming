#!/usr/bin/python3

import calculator_1
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = (sys.argv[2])

    if c == '+':
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))

    elif c == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))

    elif c == '*':
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))

    else:
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
