#! /usr/bin/env python3
import sys
line = sys.stdin.readlines()[0]
flag = ""
for char in line:
    for code in range(0, 127):
        if ord(char) - (code << 8) <= 126 and ord(char) - (code << 8) > 0:
            flag = flag + chr(code) + chr(ord(char) - (code << 8))
            break

print(flag)    

