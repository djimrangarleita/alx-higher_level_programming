#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

print('------------')


my_square2 = Rectangle.square(0)
print("Area: {} - Perimeter: {}".format(my_square2.area(), my_square2.perimeter()))
print(my_square2)

print('---------------')

my_square3 = Rectangle.square('I am')
print("Area: {} - Perimeter: {}".format(my_square3.area(), my_square3.perimeter()))
print(my_square3)
