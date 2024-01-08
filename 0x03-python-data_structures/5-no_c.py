#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for x in my_string:
        if x not in 'cC':
            new_str += x

    return new_str
