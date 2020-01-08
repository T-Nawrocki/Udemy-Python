# pytz is the module referred to at the end of the last lecture notes
# it is a module containing powerful tools for handling timezones

# it is not part of the standard library—you need to install the package separately
# essentially, to do this:
#   close your project
#   from the welcome screen of intellij, configure > structure for new projects
#   go to SDKs tab on the left
#   select the SDK (software development kit) you want to install packages to
#   go to the packages tab on the right hand pane
#   click the + button
#   select your package from the list, then install package
#   when you've installed the package, you should be able to import the module without an error message

import pytz
import datetime

country = "Europe/Moscow"  # format matters, see below for list of all timezones
tz_to_display = pytz.timezone(country)  # creates a tzinfo object with timezone information for location specified

# returns current datetime from tzinfo provided
local_time = datetime.datetime.now(tz=tz_to_display)

print(f"The time in {country} is {local_time}")
print(f"UTC is {datetime.datetime.utcnow()}")

print("=" * 40)

# lists all timezones available using pytz
for timezone in pytz.all_timezones:
    print(timezone)

# note that these are not necessarily the most user-friendly labels for these timezones,
# so we may need to do a bit of work to make them usable as a list to search from, if used for user input

print("=" * 40)

# lists country names available in pytz
# country names is a dictionary with the two letter country code as key
for x in sorted(pytz.country_names):
    print(f"{x}: {pytz.country_names[x]}")

# can also list all timezones for a given country
# unfortunately, the timezone dictionary does not use all the same keys as the country names dictionary
# eg BV appears in the countries dictionary but not the timezones one (Bouvet Island is uninhabited)
# so we cannot iterate through the countries dictionary and show timezones, because it will throw
# an error when there's a country key which doesn't have a corresponding timezone value
# but all keys in timezones dictionary appear in the countries one, so can use that just fine
for x in sorted(pytz.country_timezones):
    print(f"{x} ({pytz.country_names[x]}): {pytz.country_timezones[x]}")

print("=" * 40)

# alternatively, we could iterate through country_names, but use .get() to return None if there is no value for the key
for x in sorted(pytz.country_names):
    print(f"{x} ({pytz.country_names[x]}): {pytz.country_timezones.get(x)}")

# the timezone data here comes from a database maintained by the IANA (internet assigned numbers authority)
# the database is kept up to date and used for most computers to keep their times updated properly,
# but windows does things a little differently sometimes

print("=" * 40)

# printing the current time for each timezone for each country:
for country in sorted(pytz.country_names):
    print(f"{country} ({pytz.country_names[country]}): ")
    if country in pytz.country_timezones:
        for tz in pytz.country_timezones[country]:
            # datetime.datetime.now() produces current datetime
            # but need a tzinfo object to be argument
            # tz is a string, but can use pytz.timezone() to get tzinfo using that string
            print(f"\t\t{tz}: {datetime.datetime.now(tz=pytz.timezone(tz))}")
    else:  # if no timezone data, print error
        print("\t\tNo timezone data.")

# the best way, in general, to deal with local times is to immediately convert them to UTC
# you can conver them back when they need to be displayed
# this is to cover things like DST changes—on a day when the clocks change, there could
# be two 1.30 am times in a single day, one with DST and one without
# converting to UTC immediately lets you know which is which, handle the time properly,
# and then convert back to whatever local time is appropriate once oyu're done manipulating the data