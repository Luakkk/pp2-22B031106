#Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta

currentdaydate = datetime.now()
yesterdaydate = currentdaydate - timedelta(days=1)
tomorrowdaydate = currentdaydate + timedelta(days=1)

print("yesterday date", yesterdaydate.strftime("%Y-%m-%d"))
print("current date", currentdaydate.strftime("%Y-%m-%d"))
print("tomorrow date", tomorrowdaydate.strftime("%Y-%m-%d"))