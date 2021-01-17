#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"


def main():
    while True:
        number = int(input("Give a number please.\n"))
        if number % 2 == 0:
            print("Your number is an even number.\n")
        else:
            print("Your number is an odd number.\n")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
