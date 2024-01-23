#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as e:
        res = None
        print("Exception: {}".format(e), file=stderr)

    return (res)
