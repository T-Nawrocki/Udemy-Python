# naive local datetime is datetime data without timezone data to go with it
# aware datetime has both datetime and timezone data

import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print(f"Naive local time is {local_time}.")
print(f"Naive UTC is {utc_time}")

aware_local_time = pytz.utc.localize(local_time).astimezone()  # converts the naive time to aware time, with timezone
aware_utc_time = pytz.utc.localize(local_time)  # UTC unless specified otherwise with .astimezone() (default system tz)

print(f"Aware local time is {aware_local_time} and the time zone is {aware_local_time.tzinfo}.")
print(f"Aware UTC is {aware_utc_time} and the time zone is {aware_utc_time.tzinfo}.")

print("=" * 40)

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)  # 1:30 am on oct 25 2015—clocks fell back an hour on this day
print(gap_time)
print(gap_time.timestamp())  # timestamp is seconds since epoch
# result here is 1445733000.0, but only if you're in UTC+0 timezones
# we're using GMT here as an example, so will hardcode this answer below
# note even in uk, this program will give different results during BST

# hardcoding this here so that our example works in any timezone without extra work just now
s = 1445733000
t = s + (60 * 60)  # s plus 1 hour

gb = pytz.timezone("GB")

# localises the timestamps above as gb timezone
# note we're using utcfromtimestamp rather than fromtimestamp because epoch starts at different times for
# different time zones—1 jan 1970 happened at differnet times in diffenret timezones
# fromtimestamp would work in UTC+0 timezones, but not elsewhere, which can be really difficult to spot as an error
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print(f"{s} seconds since epoch is {dt1}")
print(f"{t} seconds since epoch is {dt2}")

# result—two different timestamps give same localised datetime
