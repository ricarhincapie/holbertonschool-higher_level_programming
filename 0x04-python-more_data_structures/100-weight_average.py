#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    divisor = sum([sec for first, sec in my_list])
    dividend = sum([first * sec for first, sec in my_list])
    return dividend / divisor
