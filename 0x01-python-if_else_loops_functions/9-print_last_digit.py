#!/usr/bin/python3

def print_last_digit(number):
    if number == 0:
        print(number, end="")
        return number
    elif number > 0:
        last = number % 10
        print(last, end="")
    else:
        last = abs(number) % 10
        print(last, end="")
    return last
