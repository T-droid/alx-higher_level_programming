#!/bin/python3

def multiple_returns(sentence):
    if not sentence:
        result = (None, 0)
        return result
    result = (len(sentence), sentence[0])
    return result
