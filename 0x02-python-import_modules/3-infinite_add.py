#!/usr/bin/python3
if __name__ == "__main__":
        import sys

        add = 0
        tmp = 0
        if len(sys.argv) < 2:
                print(0)
        else:
                for arg in range(1, len(sys.argv)):
                        tmp = int(sys.argv[arg])
                        add = add + tmp
                print(add)
