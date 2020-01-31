import time
import random

# time, datetime and calendar are the three primary modules for dealing with time in the python standard library
# time is best used for elapsed time
# datetime is best for dates and absolute times
# calendar is best for calendars (surprisingly)

# time is generally measured in programming as seconds from a certain start point.
# This start point is called the *epoch*
# the epoch for unix is 1 Jan 1970
print(time.gmtime(0))  # gmtime() provides epoch for current Operating System

# because 32 bit signed integers have a max value, we will eventually hit a point where
# there have been too many seconds since the epoch to continue counting this way.
# currently, this is in 2038, but it may differ by system etc

print(time.localtime())  # localtime() returns system time as a struct_time (which is a named tuple—see more below)
print(time.time())  # time() returns number of seconds since epoch

print("=" * 40)

time_here = time.localtime()
print(time_here)
print("Year:", time_here[0], time_here.tm_year)  # can access data within the tuple either using an index,
print("Month:", time_here[1], time_here.tm_mon)  # or by using the appropriate .tm_xxxx name
print("Day:", time_here[2], time_here.tm_mday)   # (this is what is meant by a "named" tuple

print("=" * 40)

# BASIC REACTION TIMER

input("Press enter to start.")

wait_time = random.randint(1, 6)  # waits for random number of seconds between 1 and 5 after pressing start
time.sleep(wait_time)
start_time = time.perf_counter()  # after waiting, binds current time to start_time
# perf_counter() used instead of time() because time() produces an actual time result, where perf_counter does not
# using an actual current time result, we could experience issues if the system clock changes between start and stop
# eg changing from standard time to daylight savings would show a reaction time of 1 hour +
# smaller inaccuracies would come in if the system clock syncs with a server during the timer being active
# perf_counter is the most precise clock in the time module, and avoids these issues by keeping things internal
# monotonic() is another precise clock which could serve a similar role to perf_counter

input("Press enter to stop.")

end_time = time.perf_counter()  # binds current time to end time

# time.localtime(x) will get the local time at absolute time x
# time.strftime() gets string from time
# it is used to turn a time into a more readable format
# there's a table in the documentation which shows the different formats whcih can be used
# %X is "Locale's appropriate time representation"
# so altogether this code reads:
# return local time equivalent of start time, then format it as a string, using %X (local time format) as the format
print(f"Started at {time.strftime('%X', time.localtime(start_time))}.")
print(f"Ended at {time.strftime('%X', time.localtime(end_time))}.")

print(f"Your reaction time was {end_time - start_time} seconds.")
