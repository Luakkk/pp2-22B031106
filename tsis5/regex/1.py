#Write a Python program that matches a string
#that has an 'a' followed by zero or more 'b''s.


import re

kxkx = input()
x = re.search(r"\ba*b", kxkx)

if x:
    print(x)