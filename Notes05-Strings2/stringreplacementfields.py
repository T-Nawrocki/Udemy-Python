# contains material from lecture 34 and 35

number = 12345
# strings and numbers can't be concatenated, but we do want to display them side by side often

number_as_string = str(number)  # the str() function can coerce a number into a string
print("number = " + number_as_string)

print("number = {0}".format(number))  # this uses a replacement field
# this is often a much more efficient method of formatting a number as a string

print("a number sequence: {0}, {1}, {2}, {3}, {4}".format(1, 2, 3, 4, 5))  # multiple replacement fields
# replacement fields don't need to be numbers, they can be pretty much any type
# replacement fields can be used more than once, and they don't need to appear in sequence
# the index of hte field is the only thing that matters for working out what data should be merged there
print(
    """Jan: {2}
    Feb: {0}
    Mar: {2}
    Apr: {1}
    May: {2}
    Jun: {1}
    Jul: {2}
    Aug: {2}
    Sep: {1}
    Oct: {2}
    Nov: {1}
    Dec: {2}"""
    .format(28, 30, 31)
)

print()
print("===========")
print()

# replacement fields can format the output
for i in range(1, 13):
    print("{0:2} squared is {1:^3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))  # ** is the "power" operator
# output field width is formatted to 2, 3 and 4 characters respectively, using {i:n}.
# output field is left aligned using {i:<n}
# output field is centred using {i:^n}

print("Pi is approximately {0:12}".format(22 / 7))  # default (15 decimals), spaced for minimum 12 characters
print("Pi is approximately {0:12f}".format(22 / 7))  # floating point (default 6 decimals) spaced for 12 chars
print("Pi is approximately {0:12.50f}".format(22 / 7))  # floating point, precision 50 decimals, spaced for 12 chars
print("Pi is approximately {0:52.50f}".format(22 / 7))  # floating point, precision 50 decimals, spaced for 52 chars
print("Pi is approximately {0:62.50f}".format(22 / 7))  # floating point, precision 50 decimals, spaced for 62 chars
print("Pi is approximately {0:72.50f}".format(22 / 7))  # floating point, precision 50 decimals, spaced for 72 chars
# note precision overrides field width, if they conflict
# ~51–53 decimals is limit for float in python. Higher than that needs decimal, but won't really need that anytime soon
print("Pi is approximately {0:<72.60f}".format(22 / 7))

for i in range(1, 13):
    print("{:2} squared is {:^3} and cubed is {:<4}".format(i, i ** 2, i ** 3))
# you can omit field index and it will default to using the data in order
# however this means you can't reuse data more than once
