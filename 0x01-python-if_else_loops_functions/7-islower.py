#!/usr/bin/python3
def islower(c):
        x = ord(c)  # Ord returns the Unicode of the char c
        if x > 96 and x < 123:
                return(True)
        else:
                return(False)
