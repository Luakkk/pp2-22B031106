#Write a Python program to calculate two date difference in seconds.

from datetime import datetime, timedelta

current = datetime.now()
tomorrow = current + timedelta(days=1)

difference = (current - tomorrow).total_seconds()
print(difference)