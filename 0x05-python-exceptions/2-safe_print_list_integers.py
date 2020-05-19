#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
        try:
                i = 0
                resta = 0
                while(i < x):
                        if type(my_list[i]) is not int:
                                i += 1
                                resta += 1
                                continue
                        print("{:d}".format(my_list[i]), end="")
                        i += 1
                print()
        except ValueError:
                print()
        return(i - resta)
