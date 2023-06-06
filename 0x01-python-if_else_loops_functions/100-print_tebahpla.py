#!/usr/bin/python3
for x in range(ord('z'), ord('a') - 1, -1):
    if x % 2 == 0:
        index = 0
    else:
        index = 32
    print('{}'.format(chr(x - index)), end='')
