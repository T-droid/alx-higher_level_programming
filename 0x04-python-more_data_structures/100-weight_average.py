#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    total_weight = 0
    weighted_sum = 0

    for score, weight in my_list:
        weighted_sum += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    average = weighted_sum / total_weight
    return average
