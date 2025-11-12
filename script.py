import time
import datetime
now=datetime.datetime.now()
print("a) Current Data and Time:",now)
print("b) Current year:",now.year)
print("c) Month of the year:",now.month)
print("d) Week number of the year:",now.isocalendar()[1])
print("e) Week day of the week:",now.strftime("%A"))
print("f) Day of the year:",now.timetuple().tm_yday)
print("g) Day of the Month:",now.day)
print("h) Day of the week(0=Monday,6=Sunday):",now.weekday())

