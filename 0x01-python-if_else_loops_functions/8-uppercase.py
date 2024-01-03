#!/usr/bin/python3
def islower(c):
    charint = ord(c)
    if (charint < 97 or charint > 122):
        return False
    return (charint >= 97 and charint <= 122)


def uppercase(str):
    for i in range(len(str)):
        char = str[i]
        if islower(char):
            char = chr(ord(char) - 32)
        print("{:s}".format(char), end="")
    print("")
