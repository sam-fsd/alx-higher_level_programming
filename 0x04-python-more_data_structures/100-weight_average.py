#!/usr/bin/python3
def weight_average(my_list=[]):
    total_sum, total_weight = 0, 0

    for row in my_list:
        total_sum += row[0] * row[1]
        total_weight += row[1]

    return total_sum / total_weight
