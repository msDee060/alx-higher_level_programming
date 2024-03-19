#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        temp = ch
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(ch) - 32)
        print("{}".format(temp), end='')
    print()
