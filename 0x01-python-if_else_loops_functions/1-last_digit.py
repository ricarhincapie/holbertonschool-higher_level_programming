#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
original_number = number
if original_number < 0:
    original_number = number * -1
last_digit = original_number % 10
if last_digit > 5:
    string = "and is greater than 5"
elif last_digit == 0:
    string = "and is 0"
elif last_digit > 0 and last_digit < 6:
    string = "and is less than 6 and not 0"
print("Last digit of {} is {} and {}".format(number, last_digit, string))
