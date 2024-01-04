#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv)
    print("{:d} {:s}".format((argc - 1), "arguments:"
          if argc > 2
          else ("argument:" if argc == 2 else "argument.")))
    for i in range(1, argc):
        print("{:d}: {:s}".format(i, argv[i]))
