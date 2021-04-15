#!/usr/bin/env python3
import sys
for line in sys.stdin:
    for char in line:
        print(ord(char), end = ' ')
