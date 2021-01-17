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
        participle = int(input("Give another number please. (participle)\n"))

        if number % participle == 0:
            print("Your number is divisible by the participle.\n")
        else:
            print("Your number is NOT divisible by the participle.\n")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
