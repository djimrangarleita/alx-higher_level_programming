#!/usr/bin/python3


"""Module that is used to parse and print text"""


def text_indentation(text):
    """Tokenize and print text"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    if len(text) < 1:
        return
    delim = text.maketrans('.?:', '...')
    text = text.translate(delim)
    tokens = text.split('. ')
    for token in tokens:
        print(token.strip())
        print()
