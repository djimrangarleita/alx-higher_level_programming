#!/usr/bin/python3
def print_last_digit(number):
    lastdigit = number % 10
    if number < 0:
        lastdigit = -1 * (number % -10)
    print(lastdigit, end="")

    return lastdigit
