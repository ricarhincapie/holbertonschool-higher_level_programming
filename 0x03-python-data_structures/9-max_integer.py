#!/usr/bin/python3
def max_integer(my_list=[]):
        if not my_list:
                return None
        if len(my_list) is 1:
                return my_list[0]
        i = 1
        maxi = 0
        for i in range(len(my_list)):
                if my_list[i - 1] >= my_list[i] and my_list[i - 1] > maxi:
                        maxi = my_list[i - 1]
        return maxi
