#!/usr/bin/python3
"""Module for append_write to a file function"""


def append_write(filename="", text=""):
    """Appends text to a specified file
    Args:
        filename (str): Is the file to open
        text (str): The text to append to the file
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        written = f.write(text)
    return written
