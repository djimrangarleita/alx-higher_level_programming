import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]

s = b"Hello"
lib.print_python_bytes(s);  #bytes
print();
print();
print();

b = b'\xff\xf8\x00\x00\x00\x00\x00\x00';
lib.print_python_bytes(b);  #bytes

print();
print();
print();

b = b'What does the \'b\' character do in front of a string literal?';
lib.print_python_bytes(b);  #bytes

print();
print();
print();

l = [b'Hello', b'World']
lib.print_python_list(l)    #list

print();
print();
print();

del l[1]
lib.print_python_list(l)    #list

print();
print();
print();

l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
lib.print_python_list(l)    #list

print();
print();
print();

l = []
lib.print_python_list(l)    #list

print();
print();
print();

l.append(0)
lib.print_python_list(l)    #list

print();
print();
print();

l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list(l)    #list

print();
print();
print();

l.pop()
lib.print_python_list(l)    #list

print();
print();
print();

l = ["Holberton"]
lib.print_python_list(l)    #list

print();
print();
print();

lib.print_python_bytes(l);  #bytes
