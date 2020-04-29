#!/usr/bin/python3
def print_last_digit(number):
        copy_number = number
        if(copy_number < 0):
                copy_number = copy_number * -1
        number = copy_number
        last_digit = number % 10
        print("{:d}".format(last_digit), end='')
        return(last_digit)
