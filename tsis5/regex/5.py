#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

kxkx = input()

x = re.match(r'^a.*b$', kxkx)
if x:
    print("match")
else:
    print ("no")