#!/usr/bin/python3
for j in range (ord('z'), ord('a') - 1, -1):
    if j % 2 != 0:
        print("{}".format(chr(j - 32)), end="")
    else:
        print(f"{chr(j)}", end="")
