Let's analyze the code:
```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```
ord function returns the unicode code of a charecter.
chr funcion returns the character from an unicode code.
<< 8 shift the number to the left by 8 bits, which is equivalent to multiplication by 2^8 or 256.
Maybe it's this python code that generate the content of the file enc based on the flag. Let's test it on the first two characters of the flag: pi. I write a python script to print all the unicode codes of all characters in the file enc.

test.py
```python
#!/usr/bin/env python3
import sys
for line in sys.stdin:
    for char in line:
        print(ord(char), end = ' ')
```

Run the command ```cat enc | ./test.py```, we get the output:
```
28777 25455 17236 18043 12598 24418 26996 29535 26990 29556 13108 25695 28518 24376 24375 13668 13368 14648 25213
```

The unicode code of p in decimal is 112, and of i is 105. 112 * 256 + 105 = 28777. Therefore, our assumption is correct.The python code generates the content of the file enc based on the flag. We just need to write a python script to convert the string in the file back to the flag.

solve.py
```python
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
```

Run the command ```cat enc | ./solve.py``` and we will get the flag:
```
picoCTF{16_bits_inst34d_of_8_75d4898b}
```
