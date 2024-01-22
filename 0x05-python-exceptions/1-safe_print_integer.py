#!/usr/bin/python3


def safe_print_integer(value):
    has_print = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        has_print = False

    return (has_print)
