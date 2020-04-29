#!/usr/bin/python3
def uppercase(str):
        string = ""
        for i in range(0, len(str)):
                if ord(str[i]) > 96 and ord(str[i]) < 123:
                        x = ord(str[i])
                        x = x - 32
                        string += chr(x)
                else:
                        string += str[i]
        print("{:s}".format(string))
