#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    has_print = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        has_print = False
        print("Exception: {}".format(e), file=stderr)

    return (has_print)
