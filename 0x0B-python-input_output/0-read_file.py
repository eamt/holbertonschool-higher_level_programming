#!/usr/bin/python3
""" Module to reads a text file"""


def read_file(filename=""):
    """Read a ext file and prints it to stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
