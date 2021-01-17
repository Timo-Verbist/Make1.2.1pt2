#!/usr/bin/env python
"""
AGE
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

from _datetime import datetime


def main():
    name = str(input("What's your name?\n"))
    age = int(input("Give your age please.\n"))
    bool = str(input("Has your birthday passed already? (y/n)\n"))

    if bool == "yes":
        hundred = datetime.now().year + 100 - age
    else:
        hundred = datetime.now().year + 100 - age -1

    print("Hi " + name + "! You will turn 100 in the year " + str(hundred) + ".\n")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
