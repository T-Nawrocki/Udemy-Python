file = "../text-samples/cities.txt"

# the process for writing is very similar to reading, except you use the "w" modifier rather than "r"

cities = ["Edinburgh", "Glasgow", "Aberdeen", "Dundee", "Perth"]

with open(file, "w") as city_file:  # note file does not need to exist already—will be created automatically
    for city in cities:
        print(city, file=city_file)  # file= defines the location to print, rather than default to console
        # side note—convention against spaces around = here, as the = is not an assignment operator here
        # intellij will warn you either way, so don't worry about it too much

# print() also has a flushed=True/False argument which defaults to False
# some background to understand what this is for:
# external devices (like a monitor) are much slower than computer memory
# when data is sent to an external device, it's actually written to a buffer and then the buffer's contents are
# transferred to the external device (hence "buffering")
# this lets a program to continue processing without waiting for the write operation to complete
# in this case, we're only writing a handful of words to a text file, but larger files which need to be written will
# take much longer (note the buffer write may still be happening after the program has finished processing and is
# showing as complete)
# Sometimes, though, you want the data to be written immediately (eg if the output is to a monitor and you want the
# user to be able to see the output immediately)
# With buffering, data could be sent from the buffer, and then immediately overwritten by subsequent
# data from the buffer
# Closing a file flushes the buffer automatically
# But to ensure that you're writing data as soon as it is processed, you use the flushed=True argument.
# This flushes the buffer whenever the write operation is performed, causing the data to be written immediately

# you will in general not have to do this much—python 3 came out in 2008, and since then computer processing has
# more than tripled in speed (even phones now have faster processing than most 2008 pcs)

# =============================

# you can write pretty much anything to a text file in one way or another, but it doesn't mean you can
# read it back in the exact same form, and may have to do some manipulation to get it back properly
imelda = "More Mayhem", "Imelda May", "2011", (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)

with open("../text-samples/imelda.txt", "w") as imelda_file:
    print(imelda, file=imelda_file)

with open("../text-samples/imelda.txt", "r") as imelda_file:
    imelda_file_content = imelda_file.read()

print(imelda_file_content)  # note this is a string, not a tuple

imelda_file_content = eval(imelda_file_content)  # converts to tuple
print(imelda_file_content)
