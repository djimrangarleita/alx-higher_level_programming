# 0x00. Python - Hello, World

## Learning Objectives
### General
- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where does the name 'Python' come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with
pycodestyle

## Tasks
### Task 0: Run Python file
Write a shell script that runs a Python script
The Python file name will be saved in the env. var $PYFILE.
`shell
guillaume@ubuntu:~/py/0x00$ cat main.py
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$
`

### Task 1: Run inline
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`

### Task 2: Hello, print
Write a Python script that prints exactly `"Python is like building a multilingual puzzle`, followed by a new line
- Use the function `print`

### Task 3: Print integer
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)
- The output of the script should be:
	- the number, followed by `Battery street`,
	- followed by a new line
- You are not allowed to cast the variable `number` into a string
- Your code must be 3 lines long
- You have to use f-strings [tips](https://realpython.com/python-f-strings/)

### Task 4: Print float
Complete the source code in order to print the float stored in the variable
`number` with a precision of 2 digits.
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py)
- The output of the program should be:
	- Float: followed by the float with only 2 digits
	- followed by a new line
- You are not allowed to cast `number` to string
- You have to use f-strings

### Task 5: Print string
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py)
- The output of the program should be:
	- 3 times the value of str
	- followed by a new line
	- followed by the 9 first characters of str
	- followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long

### Task 6: Play with strings
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`

- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py)
- You are not allowed to use any loops or conditional statements.
- You have to use the variables `str1` and `str2` in your new line of code
- Your program should be exactly 5 lines long

### Task 7: Copy - Cut - Paste
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)

- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- `word_first_3` should contain the first 3 letters of the variable `word`
- `word_last_2` should contain the last 2 letters of the variable `word`
- `middle_word` should contain the value of the variable `word` without the first and last letters

### Task 8: Create a new sentence
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line.

- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals

### Task 9: Easter Egg
Write a Python script that prints "The Zen of Python", by TimPeters, followed by a new line.

- Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

### Task 10: Linked list cycle
**Technical interview preparation:**

- You are not allowed to google anything
- Whiteboard first
- This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution's runtime fast enough, does your solution require extra memory usage / mallocs, etc.
Write a function in C that checks if a singly linked list has a cycle in it.

- Prototype: `int check_cycle(listint_t *list);`
- Return: `0` if there is no cycle, `1` if there is a cycle
Requirements:

- Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`
