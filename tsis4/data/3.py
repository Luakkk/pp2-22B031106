#Write a Python program to drop microseconds from datetime.

from datetime import datetime, timedelta

current = datetime.now()
currentsec = current.replace(microsecond=0)

print(currentsec)