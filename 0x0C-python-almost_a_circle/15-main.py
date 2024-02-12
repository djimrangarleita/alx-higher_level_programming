#!/usr/bin/python3
""" 15-main """
from models.square import Square
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    s1 = Square(50)
    s2 = Square(12, 3, 4, 89)
    Square.save_to_file([s1, s2])

    with open("Rectangle.json", "r") as file:
        print(file.read())

    print('\n------------------\n')
    with open("Square.json", "r") as f:
        print(f.read())
