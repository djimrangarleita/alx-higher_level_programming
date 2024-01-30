# 0x08. Python - More Classes and Objects

## Resources

- [Object Oriented Programming (Read everything until the paragraph](https://python.swaroopch.com/oop.html) "Inheritance"(excluded))
- [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) _(Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: "General Introduction," "First-class Everything," "A Minimal Class in Python," "Attributes," "Methods," "The `__init__` Method" "Data Abstraction, Data Encapsulation, and Information Hiding," `__str__`- and `__repr__`-Methods," "Public- Protected- and Private Attributes," & "Destructor")_
- [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
- [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php) _(Mainly the last part "Public instead of Private Attributes")_
- [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)

## Learning Objectives

- Why Python programming is awesome
- What is OOP
- "first-class everything"
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- What are the special `__str__` and `__repr__` methods and how to use them
- What is the difference between `__str__` and `__repr__`
- What is a class attribute
- What is the difference between a object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is and what does contain `__dict__` of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the `getattr` function

## Tasks

### Tasks 0: Simple rectangle
Write an empty class `Rectangle` that defines a rectangle:

You are not allowed to import any module

### Tasks 1: Real definition of a rectangle
Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)

- Private instance attribute: `width`:
	- property `def width(self):` to retrieve it
	- property setter `def width(self, value):` to set it:
		- `width` must be an integer, otherwise raise a `TypeError` exception `with the message width must be an integer`
		- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
	- property `def height(self):` to retrieve it
	- property setter `def height(self, value):` to set it:
		- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
		- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- You are not allowed to import any module

### Task 2: Area and Perimeter
Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)

- Private instance attribute: `width`:
	- property `def width(self):` to retrieve it
	- property setter `def width(self, value):` to set it:
		- `width` must be an integer, otherwise raise a `TypeError` exception `with the message width must be an integer`
		- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
	- property `def height(self):` to retrieve it
	- property setter `def height(self, value):` to set it:
		- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
		- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
	- if `width` or `height` is equal to `0`, perimeter is equal to `0`
- You are not allowed to import any module

### Task 3: String representation
Write a class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)

- Private instance attribute: `width`:
	- property `def width(self):` to retrieve it
	- property setter `def width(self, value):` to set it:
		- `width` must be an integer, otherwise raise a `TypeError` exception `with the message width must be an integer`
		- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
	- property `def height(self):` to retrieve it
	- property setter `def height(self, value):` to set it:
		- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
		- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
	- if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
	- if `width` or `height` is equal to 0, return an empty string
- You are not allowed to import any module

### Task 4: Eval is magic
Write a class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)

- Private instance attribute: `width`:
	- property `def width(self):` to retrieve it
	- property setter `def width(self, value):` to set it:
		- `width` must be an integer, otherwise raise a `TypeError` exception `with the message width must be an integer`
		- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
	- property `def height(self):` to retrieve it
	- property setter `def height(self, value):` to set it:
		- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
		- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
	- if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
	- if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- You are not allowed to import any module

### Task 5: Detect instance deletion
Write a class `Rectangle` that defines a rectangle by: (based on `4-rectangle.py`)

- Private instance attribute: `width`:
	- property `def width(self):` to retrieve it
	- property setter `def width(self, value):` to set it:
		- `width` must be an integer, otherwise raise a `TypeError` exception `with the message width must be an integer`
		- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
	- property `def height(self):` to retrieve it
	- property setter `def height(self, value):` to set it:
		- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
		- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
	- if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
	- if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- You are not allowed to import any module

### Task 6: How many instances
Write a class `Rectangle` that defines a rectangle by: (based on `5-rectangle.py`)

- Private instance attribute: `width`:
	- property `def width(self):` to retrieve it
	- property setter `def width(self, value):` to set it:
		- `width` must be an integer, otherwise raise a `TypeError` exception `with the message width must be an integer`
		- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
	- property `def height(self):` to retrieve it
	- property setter `def height(self, value):` to set it:
		- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
		- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
	- Initialized to `0`
	- Incremented during each new instance instantiation
	- Decremented during each instance deletion
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
	- if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
	- if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- You are not allowed to import any module

### Task 7: Change representation
Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)

- Private instance attribute: `width`:
	- property `def width(self):` to retrieve it
	- property setter `def width(self, value):` to set it:
		- `width` must be an integer, otherwise raise a `TypeError` exception `with the message width must be an integer`
		- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
	- property `def height(self):` to retrieve it
	- property setter `def height(self, value):` to set it:
		- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
		- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
	- Initialized to `0`
	- Incremented during each new instance instantiation
	- Decremented during each instance deletion
- Public class attribute `print_symbol`:
	- Initialized to `#`
	- Used as symbol for string representation
	- Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
	- if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
	- if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- You are not allowed to import any module

### Task 8: Compare rectangle
Write a class `Rectangle` that defines a rectangle by: (based on `7-rectangle.py`)

- Private instance attribute: `width`:
	- property `def width(self):` to retrieve it
	- property setter `def width(self, value):` to set it:
		- `width` must be an integer, otherwise raise a `TypeError` exception `with the message width must be an integer`
		- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
	- property `def height(self):` to retrieve it
	- property setter `def height(self, value):` to set it:
		- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
		- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
	- Initialized to `0`
	- Incremented during each new instance instantiation
	- Decremented during each instance deletion
- Public class attribute `print_symbol`:
	- Initialized to `#`
	- Used as symbol for string representation
	- Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
	- if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
	- if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
	- `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
	- `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
	- Returns `rect_1` if both have the same area value
- You are not allowed to import any module

### Task 9: A square is a rectangle
Write a class `Rectangle` that defines a rectangle by: (based on `8-rectangle.py`)

- Private instance attribute: `width`:
	- property `def width(self):` to retrieve it
	- property setter `def width(self, value):` to set it:
		- `width` must be an integer, otherwise raise a `TypeError` exception `with the message width must be an integer`
		- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
	- property `def height(self):` to retrieve it
	- property setter `def height(self, value):` to set it:
		- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
		- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
	- Initialized to `0`
	- Incremented during each new instance instantiation
	- Decremented during each instance deletion
- Public class attribute `print_symbol`:
	- Initialized to `#`
	- Used as symbol for string representation
	- Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
	- if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
	- if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
	- `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
	- `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
	- Returns `rect_1` if both have the same area value
- Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`
- You are not allowed to import any module

### Task 10: N queens **advanced**
The N queens puzzle is the challenge of placing N non-attacking queens on an NxN chessboard. Write a program that solves the N queens problem.

- Usage: `nqueens N`
	- If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
- where N must be an integer greater or equal to `4`
	- If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
	- If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
- The program should print every possible solution to the problem
	- One solution per line
	- Format: see example
	- You don't have to print the solutions in a specific order
- You are only allowed to import the `sys` module
- Read: [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29), [Backtracking](https://en.wikipedia.org/wiki/Backtracking)
