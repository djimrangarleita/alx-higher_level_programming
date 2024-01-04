#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = [x for x in dir(hidden_4) if not x.startswith("__")]
    for name in names:
        print(name)
