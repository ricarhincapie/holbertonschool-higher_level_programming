#!/usr/bin/python3
"""My main for personal testing
"""

from models.rectangle import Rectangle

if __name__ == "__main__":
    figure = Rectangle(2, 3)
    print(figure)
    figure.update(mama=20)
    print(  figure.__dict__
