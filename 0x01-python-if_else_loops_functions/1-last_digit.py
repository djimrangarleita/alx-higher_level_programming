#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is {: d}".format(number, number % 10))
