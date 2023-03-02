#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

kxkx = input()

x = '[A-Z_][a-z_]+'

kxkx = re.findall(x, input())
if kxkx:
    print(*kxkx, ' ')