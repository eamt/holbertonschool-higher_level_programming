#!/usr/bin/python3
"""
    text_indentation module.
"""


def text_indentation(text):
    """Print  text with 2 new lines after each characters: ., ? and :.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    spc = 0
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print("{:s}".format(i), end="")
            print()
            print()
            spc = 1
        else:
            if not spc:
                print("{:s}".format(i), end="")
            else:
                if i == ' ' or i == '\t':
                    continue
                print("{:s}".format(i), end="")
                spc = 0
