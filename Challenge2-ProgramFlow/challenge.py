# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Examples of the input you may get are:
#    127.0.0.1
#    .192.168.0.1
#    10.0.123456.255
#    172.16
#    255
#
# So your program should work even with invalid IP Addresses. We're just interested in the
# number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input to test:
#    .123.45.678.91
#    123.4567.8.9.
#    123.156.289.10123456
#    10.10t.10.10
#    12.9.34.6.12.90
#    '' - that is, press enter without typing anything
#
# This challenge is intended to practise for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.

ip_address = input("Please enter an IP address: ")

segments = []  # segment list will contain length of each segment. number of segments will be len(segments)
char_counter = 0  # counter to track how many chars in the current segment

while ip_address == "":  # if no input received, prompts for input again
    ip_address = input("You didn't type anything. Please enter an IP address: ")

for char in ip_address:
    if char != ".":  # if we haven't reached segment boundary, increment counter
        char_counter += 1
    else:  # at segment boundary, add counter to list and reset to 0
        segments.append(char_counter)
        char_counter = 0
segments.append(char_counter)  # adds final segment character count to list

number_of_segments = len(segments)

print(f"There are {number_of_segments} segments in total.")
for index, segment in enumerate(segments, start=1):
    print(f"Segment {index} has {segment} characters.")
    # enumerate creates a list of tuples: number at specified start (implicit 0 if none) and element of the input list
    # trying to do this by explicitly calling the index of segment instead of using enumerate wasn't working
    # and in any case that approach is apparently poor form in python
    # so I'm not worrying about it too much
