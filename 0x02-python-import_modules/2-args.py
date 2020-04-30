#!/usr/bin/python3
if __name__ == "__main__":
        import sys
        lenght = len(sys.argv)
        if lenght == 1:
                print("{:d} arguments.".format(lenght - 1))
        elif lenght == 2:
                print("{:d} argument:".format(lenght - 1))
                print("{:d}: {:s}".format(lenght - 1, sys.argv[1]))
        else:
                print("{:d} arguments:".format(lenght - 1))
                for arg in range(1, lenght):
                        print("{:d}: {:s}".format(arg, sys.argv[arg]))
