#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in roman_string[::-1]:
        value = roman_numerals[char]

        if value >= prev_value:
            total += value
        else:
            total -= value

        prev_value = value

    return total
