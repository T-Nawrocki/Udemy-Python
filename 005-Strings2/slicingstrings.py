# contains content from lectures 28-32

parrot = "Norwegian Blue"

# slicing creates a substring with multiple characters, using a start, stop and step value

print(parrot[0:6])  # Norweg (start at 0, stop at 6. No step value)
# as with ranges, the stop value is not included in the range

print(parrot[3:5])  # we
print(parrot[:9])  # Norwegian (implicit string start start value)
print(parrot[10:])  # Blue (implicit string end stop value)
print(parrot[:])  # Norwegian Blue (both start and stop implicit, give full string, not sure why you'd ever do this)
# apparently doing this is useful for lists because it creates a copy of the list, but not used much with strings
print(parrot[:6] + parrot[6:])  # Norwegian Blue (can concatenate slices like any other string)

print(parrot[-4:-2])  # Bl (can use negative indexes for slicing)
print(parrot[-4:2])  # no output (index 2 is before index -4 (= index 10), so range is invalid)
print(parrot[-4:12])  # Bl (with valid range, can mix negative and positive indexes)
print(parrot[-14:])  # Norwegian Blue

print(parrot[0:6:2])  # Nre (start at 0, continue up to 6, step by 2)
print(parrot[:6:3])  # Nw (start at beginning of string, stop before 6, step by 3)

#######################################################################################################

number = "1,234,567,890"
print(number[1::4])  # ,,, (not so useful, but shows using a slice to pick out separators from a number)

number = "9,223;372:036 854,775;807"
separators = number[1::4]  # can bind slice to variable
print(separators)
# next bit uses some stuff we'll be getting to in the rest of the course
# creates a string which iterates through separators, and appends the char if it is not in separators, or " " if it is
# then .split() turns that string into a list of the values separated by " " (I think)
values = "".join(char if char not in separators else " " for char in number).split()
# prints a list containing the elements of values
print([int(val) for val in values])

###############################################

#                    1         2
#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]  # zyxwvutsrqponmlkjihgfedcb (can slice backwards by using a negative step)
# note that a is not included because the stop value for the range is not included in the range
print(backwards)

backwards_in_full = letters[25::-1]  # zyxwvutsrqponmlkjihgfedcba (implicit stop takes us all the way to the boundry)
# this version includes a
print(backwards_in_full)

backwards = letters[::-1]  # this syntax is a python idiom/convention. It reverses a string in full

#################################################

print()
print("===================")
print()

# Mini challenge—
# (a) create a slice that's qpo;
# (b) create a slice that's edcba;
# (c) create a slice that's the last 8 chars in reverse order

qpo = letters[16:13:-1]
print(qpo)

edcba = letters[4::-1]
print(edcba)

last_eight_reversed = letters[:-9:-1]
print(last_eight_reversed)

###############################################

# SLICING IDIOMS

string = "1234567890"

reverse_string = string[::-1]
last_n_chars = string[-4:]  # where n = 4
last_char = string[-1:]
first_char = string[:1]  # does not give an error if the string is empty, so sometimes preferred to string[0]

