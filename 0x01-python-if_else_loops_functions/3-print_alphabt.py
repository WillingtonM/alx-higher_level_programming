#!/usr/bin/python3
for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) == 'e' or chr(letter) == 'q':
        continue
    else:
        print("{:s}".format(chr(letter)), end="")
