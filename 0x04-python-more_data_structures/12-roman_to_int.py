#!/usr/bin/python3
def roman_to_int(roman_string):
    from functools import reduce
    if not roman_string or type(roman_string) is not str:
        return 0

    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum_list = []
    for i in range(len(roman_string)):
        for key in roman:
            if roman_string[i] is key:
                sum_list.append(roman.get(roman_string[i]))
    # for i in range(len(sum_list)):
        # print("{}".format(sum_list[i]))
    final_sum = 0
    i = 0
    while i in range(len(sum_list)):
        if i < len(sum_list) - 1 and sum_list[i] < sum_list[i + 1]:
            final_sum += (sum_list[i + 1] - sum_list[i])
            i += 2
        else:
            final_sum += sum_list[i]
            i += 1
    return final_sum
