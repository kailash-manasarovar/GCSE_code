import datetime as dt
import time as tm


# time returns the current time in seconds since the Epoch. (January 1st, 1970)
print(tm.time())


# convert the timestamp to datetime.
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)


print(dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second)

print("Year = " + str(dtnow.year))
print("Month = " + str(dtnow.month))
print("Day = " + str(dtnow.day))
print("Hour = " + str(dtnow.hour))
print("Minute = " + str(dtnow.minute))
print("Second = " + str(dtnow.second))


# create a timedelta of 100 days
delta = dt.timedelta(days = 100)
print(delta)
today = dt.date.today()
print(today)
print(today - delta) # the date 100 days ago
print(today > today-delta) # compare dates