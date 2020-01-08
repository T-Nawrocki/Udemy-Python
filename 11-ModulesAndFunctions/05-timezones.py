# datetime should be used for any occasion where you care about dates as well as times
# time does technically include dates, if you need them incidentally,
# but it's not as useful as datetime if you're using them heavily
import datetime

# first, though, we're going to look at timezone support in the time module
# these are primarily handled using timezone and tzname
# note that these are not functions—no need for ()
import time

# timezone returns number of seconds offset from UTC (negative for UTC-x, positive for UTC+x)
# timezone calculates using Non-DST offset, so you have to apply DST separately
print(time.timezone)

# tzname returns a tuple containing two strings
# the first string is the Non-DST timezone name
# the second string is the DST timezone name
print(time.tzname)

# before relying on the DST timezone name in tzname, you first need to check the value of time.daylight
# if daylight != 0, the timezone has a DST equivalent, and the tzname second string can be trusted
# otherwise, you shouldn't use the second string
print(time.daylight)

print("=" * 40)
# ON TO DATETIME
print("=" * 40)

# datetime.datetime is a class which takes minimally three arguments (year, month, day)
print(datetime.datetime.today())  # .today() returns current date
print(datetime.datetime.now())  # .now() returns current datetime in specified timezone (defaults to current timezone)
print(datetime.datetime.utcnow())  # .utcnow() returns current datetime in utc

# timezone information for .now() is in the form of tzinfo
# however, tzinfo is an abstract class (more on that later)
# for now, that means that the information is available in python, but not implemented directly
# this is because timezones are weird and mean differnet things to different people
# so it has been left to the individual developer to implement tzinfo as they see fit
# however, there is another module (not in the standard library) which provides a lot of functionality for timezones
# this will be handled in the next video, as it must be installed separately
