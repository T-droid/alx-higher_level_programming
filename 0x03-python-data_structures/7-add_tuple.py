#!/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    cp_tup_a = (tuple_a[0] if len(tuple_a) > 0 else 0, tuple_a[1] if len(tuple_a) > 1 else 0)
    cp_tup_b = (tuple_b[0] if len(tuple_b) > 0 else 0, tuple_b[1] if len(tuple_b) > 1 else 0)

    result = (cp_tup_a[0] + cp_tup_b[0], cp_tup_a[1] + cp_tup_b[1])
    return result
