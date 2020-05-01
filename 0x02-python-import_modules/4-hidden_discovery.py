#!/usr/bin/python3
if __name__ == "__main__":

        import hidden_4
        content = dir(hidden_4)
        for line in content:
                if line[0] != '_':
                        print(line)
