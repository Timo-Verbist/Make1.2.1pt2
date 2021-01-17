#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"


def main():
    number = int(input("Give a number please.\n"))
    participle = int(input("Give another number from 0 to 9 please.\n"))
    array = ["divisible", "not divisible", "not divisible", "not divisible", "not divisible", "not divisible", "not divisible", "not divisible", "not divisible"]

    print("\nYour number is " + array[number % participle] + ".")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
