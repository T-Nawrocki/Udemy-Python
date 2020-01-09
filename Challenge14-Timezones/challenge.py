# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

options = {"1": ("Aden", "Asia/Aden"),
           "2": ("Astrakhan", "Europe/Astrakhan"),
           "3": ("Darwin", "Australia/Darwin"),
           "4": ("Halifax", "America/Halifax"),
           "5": ("Iqaluit", "America/Iqaluit"),
           "6": ("Ljubljana", "Europe/Ljubljana"),
           "7": ("Mogadishu", "Africa/Mogadishu"),
           "8": ("Sakhalin", "Asia/Sakhalin"),
           "9": ("Tripoli", "Africa/Tripoli")}

# creates a dictionary of locations, with the keys from options dictionary as the values for this dictionary
# used for comparisons to allow user to input name of location, rather than just key number
location_list = {}
for key in options:
    location_list[options[key][0].upper()] = key  # .upper() used to make comparison case-insensitive

print("List of available timezones:")
for key in sorted(options.keys()):
    print(f"\t{key}.\t {options[key][0]}")

print()

while True:
    selection = input("Select a timezone, or enter 0 to quit: ")

    if selection == "0":
        break

    elif (selection not in options.keys()) and (selection.upper() not in location_list.keys()):
        print("That is not a timezone I recognise. Please try again, selecting a timezone from the list above.")

    else:
        # if user entered name of location, not key number, set selection to corresponding key number
        if selection not in options.keys():
            selection = location_list[selection.upper()]

        selected_time = datetime.datetime.now(tz=pytz.timezone(options[selection][1]))
        local_time = datetime.datetime.now()
        utc_time = datetime.datetime.utcnow()

        # this could probably be compressed a lot, but not sure how to make reusable format
        # none of the built in ones seemed to have the format I was looking for,
        # so seemed like a decent exercise to do it myself this way
        print(f"The current time in {options[selection][0]} is: "
              f"{datetime.datetime.strftime(selected_time, '%X')} on "  # time
              f"{datetime.datetime.strftime(selected_time, '%A')} "  # day of week
              f"{datetime.datetime.strftime(selected_time, '%d').lstrip('0')} "  # day of month
              f"{datetime.datetime.strftime(selected_time, '%B')} "  # month
              f"{datetime.datetime.strftime(selected_time, '%Y')}")  # year
        print(f"The local time is: "
              f"{datetime.datetime.strftime(local_time, '%X')} on "  # time
              f"{datetime.datetime.strftime(local_time, '%A')} "  # day of week
              f"{datetime.datetime.strftime(local_time, '%d').lstrip('0')} "  # day of month
              f"{datetime.datetime.strftime(local_time, '%B')} "  # month
              f"{datetime.datetime.strftime(local_time, '%Y')}")  # year
        print(f"Current UTC time is: "
              f"{datetime.datetime.strftime(utc_time, '%X')} on "  # time
              f"{datetime.datetime.strftime(utc_time, '%A')} "  # day of week
              f"{datetime.datetime.strftime(utc_time, '%d').lstrip('0')} "  # day of month
              f"{datetime.datetime.strftime(utc_time, '%B')} "  # month
              f"{datetime.datetime.strftime(utc_time, '%Y')}")  # year
        print()


