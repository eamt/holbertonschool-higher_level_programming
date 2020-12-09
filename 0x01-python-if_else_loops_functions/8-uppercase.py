#!/usr/bin/python3
def uppercase(str):
    for i in str:
        uniCode = ord(i)
        if uniCode >= 97 and uniCode <= 122:
            i = chr(uniCode - 32)
        print("{}".format(i), end="")
    print("")
