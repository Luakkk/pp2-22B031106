#Write a Python program to subtract five days from current date.

from datetime import timedelta, datetime

current = datetime.now()
fiveminus = current - timedelta(days=5)

print("today", current.strftime("%Y-%m-%d"))
print("5 days ago", fiveminus.strftime("%Y-%m-%d"))