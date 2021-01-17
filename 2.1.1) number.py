#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"


def main():
    number = int(input("Give a number please.\n"))
    array = ["even", "odd"]

    print("\nYour number is an " + array[number % 2] + " number.")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
