#!/usr/bin/python3
""" module for magic calculation """


def magic_calculation(a, b):
    """magic calculation
    Args:
        a(int): first integer
        b(int): second integer
        """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
