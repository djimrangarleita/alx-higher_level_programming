#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    calculator = {"+": add, "-": sub, "*": mul, "/": div}
    op = argv[2]

    if op not in calculator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    print("{:d} {:s} {:d} = {:d}".format(a, op, b, calculator[op](a, b)))
