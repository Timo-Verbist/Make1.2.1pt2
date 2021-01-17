#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"


def main():
    name = str(input("Give your name please.\n"))
    birth = str(input("Give your birthdate please.\n"))

    print("So your name is " + name + " and you're born on " + birth + "?")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
